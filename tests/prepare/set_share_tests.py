import openpyxl
import xlwings as xw
from tqdm import tqdm
import json
from decimal import Decimal, ROUND_HALF_UP
from ..parameters import FILE_PATH, COUNTRY_CELL, FILTER_CELL, COUNTRIES, FILTERS, S_INDICATOR_MAPPING, JSON_FILE_SHARE

# Decided to use Decimal for rounding to avoid errors when rounding (e.g., 12.05 -> 12.0 instead of 12.1)
def round_number(value, decimals):
    if value is None:
        return None
    decimal_value = Decimal(str(value))
    rounding_format = f'0.{"0" * decimals}'
    return float(decimal_value.quantize(Decimal(rounding_format), rounding=ROUND_HALF_UP))


def format_number(value, indicator, decimals=3):
    # Check for None or empty string before trying to split
    if value in [None, '']:
        return None

    if isinstance(value, str) and ',' in value:
        number_strings = value.split(',')
        formatted_numbers = []
        for index, num_str in enumerate(number_strings):
            num_str = num_str.strip()
            if num_str.lower() == 'null':
                formatted_numbers.append(None)
            else:
                # Accounting for the year value
                if index == 0:
                    try:
                        formatted_numbers.append(int(num_str))
                    except ValueError:
                        formatted_numbers.append(num_str)
                else:
                    formatted_numbers.append(process_number_for_rounding(num_str, decimals))
        # Removing trailing None values and Nones showing up at the beginning of the array
        while formatted_numbers and formatted_numbers[-1] is None:
            formatted_numbers.pop()
        start_index = 1
        while start_index < len(formatted_numbers) and formatted_numbers[start_index] is None:
            start_index += 1
        formatted_numbers = [formatted_numbers[0]] + formatted_numbers[start_index:]

        return formatted_numbers
    
    # Process a single number or string
    return process_number_for_rounding(value, decimals)


def process_number_for_rounding(num_str, decimals):
    try:
        float_value = float(num_str)
        if float_value == 0.0:
            return None
    except (TypeError, ValueError):
        # Accounting for ordinal numbers
        return num_str

    str_value = str(float_value)

    if str_value.startswith("-0.0") or str_value.startswith("0.0") or 'e' in str_value or 'E' in str_value:
            # For exponential numbers:
        if 'e' in str_value or 'E' in str_value:
            mantissa, exponent = str_value.split('e')
            exponent = int(exponent)

            if exponent < 0:
                not_zero_index = abs(exponent)+1
            else:
                significant_digits = len(mantissa.replace('.', '').rstrip('0'))
                not_zero_index = significant_digits - 1
        else:
            not_zero_index = next((i for i, char in enumerate(str_value) if char not in '0.-'), None)

        # For when a non-zero index is found
        if not_zero_index is not None:
            return round_number(float_value, not_zero_index)
        else:
            return round_number(float_value, decimals)

    if '.' in str_value:
        return round_number(float_value, decimals)

    return float_value

def modify_and_save_excel(file_path, cell1_address, cell2_address, new_value1, new_value2):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook["Tests"]
    sheet[cell1_address].value = new_value1
    sheet[cell2_address].value = new_value2
    workbook.save(file_path)

def recalculate_excel(file_path):
    app = xw.App(visible=False)
    workbook = app.books.open(file_path)
    sheet = workbook.sheets[0]
    cell = sheet.range('A1')
    original_value = cell.value
    temp_value = 0 if original_value is None else original_value + 1
    cell.value = temp_value
    cell.value = original_value
    workbook.save()
    workbook.close()
    app.quit()

def prepare_data(combination):
    country, filter_, indicator = combination
    prepared_data = {"country": country, "filter": filter_, "indicator": indicator}
    return prepared_data

def apply_changes_to_excel(prepared_data):
    app = xw.App(visible=False)
    workbook = app.books.open(FILE_PATH)
    sheet = workbook.sheets[0]

    results = []
    # Setting progress bar to show in terminal
    for data in tqdm(prepared_data, desc="Processing", unit="combination"):
        try:
            country = data["country"]
            filter_ = data["filter"]
            indicator = data["indicator"]

            sheet.range(COUNTRY_CELL).value = country
            sheet.range(FILTER_CELL).value = filter_

            workbook.app.calculate()  # Needed to recalculate formulas before retrieving the values

            target_column, target_row = S_INDICATOR_MAPPING.get(indicator, ("F", 3))
            target_cell_address = f"{target_column}{target_row}"
            
            cell_value = sheet.range(target_cell_address).value
            formatted_values = format_number(cell_value, indicator, decimals=3)

            data["values"] = formatted_values if isinstance(formatted_values, list) else [formatted_values]
            results.append(data)

        except Exception as e:
            print(f"Error processing {data}: {e}")

    workbook.close()
    app.quit()

    return results


# Executing the script
if __name__ == "__main__":
    combinations = [(country, filter_, indicator) for country in COUNTRIES for filter_ in FILTERS for indicator in S_INDICATOR_MAPPING.keys()]
    
    prepared_data = [prepare_data(combination) for combination in combinations]

    all_results = apply_changes_to_excel(prepared_data)

    with open(JSON_FILE_SHARE, 'w') as json_file:
        json.dump(all_results, json_file, indent=2)

    print(f"Results have been written to {JSON_FILE_SHARE}")