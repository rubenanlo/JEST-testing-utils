import encodeFilterId from "data/helpers/encodeFilterId";

export const extractValues = (dataArray) =>
  dataArray.map(({ values }) => values);

const findDataId = (data, name) =>
  data.find((item) => item.name === name).dataId;
const findCategoryId = (data, id, condition = () => true) =>
  data.find((item) => item.id === id && condition(item)).categoryId;

export const getAllObservations = (data) =>
  Object.values(data)
    .flat()
    .slice(1)
    .filter((value) => value !== null && value !== 0);

const getValues = (data, country, indicator, filter, condition, field) => {
  const indicatorId = findCategoryId(
    data.assessmentsData,
    indicator,
    condition
  );
  const countryId = findDataId(data.countriesData, country);
  const filterId = encodeFilterId(filter, field);
  const key = `${countryId}_${indicatorId}_${filterId}`;

  if (field === "potential") {
    return Object.values(data.potentialData[key] || []).flat();
  }
  if (field === "tradeoff") {
    return Object.values(data.tradeoffData[key] || []).flat();
  }
  return Object.values(data.timeSeriesData[key] || []).flat();
};

export const getGeneralValues = (country, indicator, filter, data) =>
  getValues(data, country, indicator, filter);

export const getShareValues = (country, indicator, filter, data) =>
  getValues(data, country, indicator, filter, (item) =>
    item.categoryId.startsWith("S")
  );

export const getAfoluEmissionsValues = (country, indicator, filter, data) =>
  getValues(
    data,
    country,
    indicator,
    filter,
    (item) => item.categoryId.startsWith("A") && item.categoryId.endsWith("E")
  );

export const getAfoluRemovalsValues = (country, indicator, filter, data) =>
  getValues(
    data,
    country,
    indicator,
    filter,
    (item) => item.categoryId.startsWith("A") && item.categoryId.endsWith("R")
  );

export const getPotentialValues = (country, indicator, filter, data) =>
  getValues(
    data,
    country,
    indicator,
    filter,
    (item) => item.categoryId.startsWith("P"),
    "potential"
  );
export const getTradeoffValues = (country, indicator, filter, data) =>
  getValues(
    data,
    country,
    indicator,
    filter,
    (item) => item.categoryId.startsWith("T"),
    "tradeoff"
  );
