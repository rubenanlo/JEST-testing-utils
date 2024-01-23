import { loadData } from "helpers/loadData.js";
import {
  getAllObservations,
  getGeneralValues,
  getShareValues,
  getAfoluEmissionsValues,
  getAfoluRemovalsValues,
  extractValues,
} from "tests/helpers/getData";

const generalData = require("tests/expected-results/general.json");
const shareData = require("tests/expected-results/share.json");
const emissionsData = require("tests/expected-results/emissions.json");
const removalsData = require("tests/expected-results/removals.json");

const totExpectedResults = [
  ...extractValues(generalData),
  ...extractValues(shareData),
  ...extractValues(emissionsData),
  ...extractValues(removalsData),
];

let timeSeriesData;
let assessmentsData;
let countriesData;

beforeAll(async () => {
  const [{ timeseries }] = await loadData(["timeseries"]);
  const [{ assessments }] = await loadData(["assessments"]);
  const [{ countries }] = await loadData(["countries"]);
  timeSeriesData = timeseries;
  assessmentsData = assessments;
  countriesData = countries;
});

it(`renders all data for the homepage section`, () => {
  expect(getAllObservations(timeSeriesData)).toHaveLength(
    getAllObservations(totExpectedResults).length
  );
});

generalData.forEach(({ country, indicator, filter, values }) => {
  it(`has the correct values for ${country}, ${indicator}, ${filter}`, () => {
    expect(
      getGeneralValues(country, indicator, filter, {
        timeSeriesData,
        assessmentsData,
        countriesData,
      })
    ).toEqual(values);
  });
});

shareData.forEach(({ country, indicator, filter, values }) => {
  it(`has the correct values for ${country}, ${indicator}, ${filter}`, () => {
    expect(
      getShareValues(country, indicator, filter, {
        timeSeriesData,
        assessmentsData,
        countriesData,
      })
    ).toEqual(values);
  });
});

emissionsData.forEach(({ country, indicator, filter, values }) => {
  it(`has the correct emissions values for ${country}, ${indicator}, ${filter}`, () => {
    expect(
      getAfoluEmissionsValues(country, indicator, filter, {
        timeSeriesData,
        assessmentsData,
        countriesData,
      })
    ).toEqual(values);
  });
});

removalsData.forEach(({ country, indicator, filter, values }) => {
  it(`has the correct removals values for ${country}, ${indicator}, ${filter}`, () => {
    expect(
      getAfoluRemovalsValues(country, indicator, filter, {
        timeSeriesData,
        assessmentsData,
        countriesData,
      })
    ).toEqual(values);
  });
});
