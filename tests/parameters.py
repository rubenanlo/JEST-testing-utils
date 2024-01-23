# This document includes all parameters to prepare all python expected results.
# Please update this file as needed for any updates by using the source excel file

# ! This params apply to all tests:

COUNTRY_CELL = "C2"
FILTER_CELL = "C3"

# ! Timeseries:
# * File path to the excel file used for testing
# File used for testing only. Before preparing the expected results, you need to
# update this excel file by firstly deleting the old data tabs (see tab named
# "original-data") and second dragging and dropping the new sheets into the
# file. Ensure that the sheet name is exactly the same as in the older version
# (i.e., homepage, potential, tradeoff, etc).
FILE_PATH = "tests/source/testing-timeseries.xlsx"

# * JSON output files:
JSON_FILE_GENERAL = "tests/expected-results/general.json"
JSON_FILE_OVERALL = "tests/expected-results/overall.json"
JSON_FILE_SHARE = "tests/expected-results/share.json"
JSON_FILE_AFOLU_EMISSIONS="tests/expected-results/emissions.json"
JSON_FILE_AFOLU_REMOVALS="tests/expected-results/removals.json"
JSON_FILE_TRADEOFF="tests/expected-results/tradeoff.json"
JSON_FILE_SOURCES="tests/expected-results/sources.json"


# * Timeseries

COUNTRIES = ["Argentina","Australia", "Brazil", "Canada", "China", "Colombia", "Ethiopia", "Finland", "Germany", "Greece", "India", "Indonesia", "Mexico", "Nepal", "Norway", "Russia", "Rwanda", "Sweden", "Turkey", "United Kingdom", "United States"]
FILTERS = ["SAR_UNFCCC", "SAR_FAO", "AR6_UNFCCC", "AR6_FAO", "AR5_UNFCCC", "AR5_FAO", "AR4_UNFCCC", "AR4_FAO"]

# Mapping to the cells where we need to retrieve the values.
G_INDICATOR_MAPPING = {
    "tot_em": ("C", 7),
    "tot_em_cap": ("D", 7),
    "rank_cap_ghg": ("E", 7),
    "rank_glob": ("F", 7),
    "share_glob": ("G", 7),
}

S_INDICATOR_MAPPING = {
    "energy": ("H", 7),
    "waste": ("I", 7),
    "ippu": ("K", 7),
    "afolu": ("L", 7),
}

AE_INDICATOR_MAPPING={'rice_cult':('M',7),'manure_manag':('N',7),'enteric_ferm':('O',7),'agric_soils':('P',7),'drain_org_soil':('Q',7),'fire_humid_trop_for':('R',7),'fire_org_soil':('S',7),'forest_fire':('T',7),'net_forest_conv':('U',7),'savanna_fire':('V',7),'other_agric':('W',7),'forestland':('X',7),'cropland':('Y',7),'grassland':('Z',7),'harv_wood':('AA',7),'liming':('AB',7),'other_land':('AC',7),'settlements':('AD',7),'wetlands':('AE',7),'other':('AK',7),'other_lucf':('AL',7),'land-us_forestry':('AM',7),'forest_grassland':('AN',7),'changes_forest_woody':('AO',7),'agriculture':('AP',7),'aband_man_lands':('AQ',7),'co2_em_rem_soil':('AR',7),'presc_burn_sav':('AS',7),}

AR_INDICATOR_MAPPING={'forestland':('AF',7),'cropland':('AG',7),'grassland':('AH',7),'harv_wood':('AI',7),'settlements':('AJ',7),'other':('AT',7),'other_lucf':('AU',7),'land-us_forestry':('AV',7),'forest_grassland':('AW',7),'changes_forest_woody':('AX',7),'aband_man_lands':('AY',7),'co2_em_rem_soil':('AZ',7),}

# ! Potential:
# * File path to the excel file used for testing
# File used for testing only. Before preparing the expected results, you need to
# update this excel file by firstly deleting the old data tabs (see tab named
# "original-data") and second dragging and dropping the new sheets into the
# file. Ensure that the sheet name is exactly the same as in the older version
# (i.e., homepage, potential, tradeoff, etc).
FILE_PATH_POTENTIAL = "tests/source/testing-potential.xlsx"

# * JSON output files:
JSON_FILE_POTENTIAL="tests/expected-results/potential.json"


# * Total observations
COUNTRIES_POTENTIAL = ["China"]
FILTERS_POTENTIAL = ["Rice Cultivation_Conventional rice farming_kg CO2e/ha-AR4", "Rice Cultivation_Conventional rice farming_kg CO2e/ha-AR5", "Rice Cultivation_Conventional rice farming_kg CO2e/ha-AR6", "Rice Cultivation_Conventional rice farming_kg CO2e/ha-SAR", "Rice Cultivation_Conventional rice farming_kg CH4/ha", "Rice Cultivation_Conventional rice farming_kg N2O/ha", "Rice Cultivation_Double rice cropping_kg CO2e/ha-AR4", "Rice Cultivation_Double rice cropping_kg CO2e/ha-AR5", "Rice Cultivation_Double rice cropping_kg CO2e/ha-AR6", "Rice Cultivation_Double rice cropping_kg CO2e/ha-SAR", "Rice Cultivation_Double rice cropping_kg CH4/ha", "Rice Cultivation_Double rice cropping_kg N2O/ha", "Rice Cultivation_Ground cover rice production system_kg CO2e/ha-AR4", "Rice Cultivation_Ground cover rice production system_kg CO2e/ha-AR5", "Rice Cultivation_Ground cover rice production system_kg CO2e/ha-AR6", "Rice Cultivation_Ground cover rice production system_kg CO2e/ha-SAR", "Rice Cultivation_Ground cover rice production system_kg CH4/ha", "Rice Cultivation_Ground cover rice production system_kg N2O/ha", "Rice Cultivation_Rapeseed-rice rotation_kg CO2e/ha-AR4", "Rice Cultivation_Rapeseed-rice rotation_kg CO2e/ha-AR5", "Rice Cultivation_Rapeseed-rice rotation_kg CO2e/ha-AR6", "Rice Cultivation_Rapeseed-rice rotation_kg CO2e/ha-SAR", "Rice Cultivation_Rapeseed-rice rotation_kg CH4/ha", "Rice Cultivation_Rapeseed-rice rotation_kg N2O/ha", "Rice Cultivation_Rice-wheat rotation_kg CO2e/ha-AR4", "Rice Cultivation_Rice-wheat rotation_kg CO2e/ha-AR5", "Rice Cultivation_Rice-wheat rotation_kg CO2e/ha-AR6", "Rice Cultivation_Rice-wheat rotation_kg CO2e/ha-SAR", "Rice Cultivation_Rice-wheat rotation_kg CH4/ha", "Rice Cultivation_Rice-wheat rotation_kg N2O/ha"]
P_INDICATOR_MAPPING={'bioch':('C',7),'duck':('D',7),'irr-awd':('E',7),'irr-cf':('F',7),'irr-cfd':('G',7),'irr-cfdii':('H',7),'irr-ci':('I',7),'irr-inter':('J',7),'irr-rf':('K',7),'irr-swd':('L',7),'irr-tswd':('M',7),'n-conv':('N',7),'n-high':('O',7),'n-low':('P',7),'n-no':('Q',7),'n-pig':('R',7),'n-urea':('S',7),'r-f':('T',7),'r-gm':('U',7),'r-till':('V',7),'straw':('W',7),'var':('X',7),'var-d':('Y',7),'nostraw':('Z',7),'notill':('AA',7),'ratoon':('AB',7),'till':('AC',7),'bdf':('AD',7),'rpf':('AE',7),'d-ditch':('AF',7),'d-mulch':('AG',7),'n-crf':('AH',7),'s-ditch':('AI',7),'s-mulch':('AJ',7),}

# ! Tradeoff:
# * File path to the excel file used for testing
# File used for testing only. Before preparing the expected results, you need to
# update this excel file by firstly deleting the old data tabs (see tab named
# "original-data") and second dragging and dropping the new sheets into the
# file. Ensure that the sheet name is exactly the same as in the older version
# (i.e., homepage, potential, tradeoff, etc).
FILE_PATH_TRADEOFF = "tests/source/testing-tradeoff.xlsx"

# * JSON output files:
JSON_FILE_TRADEOFF="tests/expected-results/tradeoff.json"


# * Total observations
COUNTRIES_TRADEOFF = ["China"]
FILTERS_TRADEOFF = ["Rice Cultivation_Conventional rice farming_Irr-CF", "Rice Cultivation_Conventional rice farming_Irr-CFD", "Rice Cultivation_Conventional rice farming_Irr-AWD", "Rice Cultivation_Double rice cropping_Irr-CF", "Rice Cultivation_Double rice cropping_Irr-CFD", "Rice Cultivation_Double rice cropping_Irr-CFDII", "Rice Cultivation_Double rice cropping_Ratoon", "Rice Cultivation_Conventional rice farming_Var", "Rice Cultivation_Conventional rice farming_Var-D", "Rice Cultivation_Rice-wheat rotation_Irr-CF", "Rice Cultivation_Rice-wheat rotation_S-DITCH", "Rice Cultivation_Rice-wheat rotation_D-DITCH", "Rice Cultivation_Conventional rice farming_Irr-CI", "Rice Cultivation_Double rice cropping_Irr-SWD", "Rice Cultivation_Double rice cropping_N-Urea", "Rice Cultivation_Double rice cropping_Irr-TSWD", "Rice Cultivation_Conventional rice farming_Irr-Inter", "Rice Cultivation_Conventional rice farming_Irr-SWD", "Rice Cultivation_Conventional rice farming_N-Urea", "Rice Cultivation_Rice-wheat rotation_Irr-CI", "Rice Cultivation_Rice-wheat rotation_N-High", "Rice Cultivation_Rice-wheat rotation_N-Conv", "Rice Cultivation_Rice-wheat rotation_NoStraw", "Rice Cultivation_Rice-wheat rotation_Straw", "Rice Cultivation_Rice-wheat rotation_D-MULCH", "Rice Cultivation_Rice-wheat rotation_S-MULCH", "Rice Cultivation_Conventional rice farming_Irr-CFDII", "Rice Cultivation_Conventional rice farming_N-Conv", "Rice Cultivation_Conventional rice farming_N-High", "Rice Cultivation_Conventional rice farming_N-Low", "Rice Cultivation_Conventional rice farming_Duck", "Rice Cultivation_Rapeseed-rice rotation_Irr-AWD", "Rice Cultivation_Rapeseed-rice rotation_Irr-CF", "Rice Cultivation_Rapeseed-rice rotation_Irr-RF", "Rice Cultivation_Rice-wheat rotation_N-CRF", "Rice Cultivation_Rice-wheat rotation_N-Low", "Rice Cultivation_Rice-wheat rotation_N-No", "Rice Cultivation_Double rice cropping_Straw", "Rice Cultivation_Double rice cropping_Irr-RF", "Rice Cultivation_Double rice cropping_NoTill", "Rice Cultivation_Double rice cropping_R-Till", "Rice Cultivation_Double rice cropping_Bioch", "Rice Cultivation_Double rice cropping_NoStraw", "Rice Cultivation_Double rice cropping_N-No", "Rice Cultivation_Conventional rice farming_Irr-RF", "Rice Cultivation_Rice-wheat rotation_Bioch", "Rice Cultivation_Conventional rice farming_N-No", "Rice Cultivation_Conventional rice farming_R-Till", "Rice Cultivation_Rice-wheat rotation_R-Till", "Rice Cultivation_Conventional rice farming_Straw", "Rice Cultivation_Conventional rice farming_Irr-TSWD", "Rice Cultivation_Rapeseed-rice rotation_Irr-Inter", "Rice Cultivation_Double rice cropping_Irr-Inter", "Rice Cultivation_Double rice cropping_N-Conv", "Rice Cultivation_Double rice cropping_N-High", "Rice Cultivation_Double rice cropping_N-Low", "Rice Cultivation_Ground cover rice production system_BDF", "Rice Cultivation_Ground cover rice production system_N-Conv", "Rice Cultivation_Conventional rice farming_N-Pig", "Rice Cultivation_Rice-wheat rotation_NoTill", "Rice Cultivation_Rice-wheat rotation_Irr-SWD", "Rice Cultivation_Rice-wheat rotation_Till", "Rice Cultivation_Rapeseed-rice rotation_NoTill", "Rice Cultivation_Rapeseed-rice rotation_Var-D", "Rice Cultivation_Rice-wheat rotation_Duck", "Rice Cultivation_Conventional rice farming_R-F", "Rice Cultivation_Conventional rice farming_R-GM", "Rice Cultivation_Conventional rice farming_Bioch", "Rice Cultivation_Ground cover rice production system_RPF", "Rice Cultivation_Ground cover rice production system_Irr-CI", "Rice Cultivation_Ground cover rice production system_N-No", "Rice Cultivation_Double rice cropping_Irr-AWD", "Rice Cultivation_Double rice cropping_N-Pig", "Rice Cultivation_Double rice cropping_Till"]
# Mapping to the cells where we need to retrieve the values.
T_INDICATOR_MAPPING={'yield':('C',7),'above_biomass':('D',7),'irrigration_wa':('E',7),}

