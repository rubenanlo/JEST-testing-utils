import { loadData } from "helpers/loadData.js";
import {
  extractValues,
  getAllObservations,
  getTradeoffValues,
} from "tests/helpers/getData";

const numberArrowMap = require("data/library/tradeoffLabel");
const expectedTradeoffData = require("tests/expected-results/tradeoff.json");

const totExpectedResults = extractValues(expectedTradeoffData);

let tradeoffData;
let assessmentsData;
let countriesData;

beforeAll(async () => {
  const [{ tradeoff }] = await loadData(["tradeoff"]);
  const [{ assessments }] = await loadData(["assessments"]);
  const [{ countries }] = await loadData(["countries"]);
  tradeoffData = tradeoff;
  assessmentsData = assessments;
  countriesData = countries;
});

it(`renders all data for the tradeoff section`, () => {
  expect(getAllObservations(tradeoffData)).toHaveLength(
    getAllObservations(totExpectedResults).length
  );
});

expectedTradeoffData.forEach(({ country, indicator, filter, values }) => {
  it(`has the correct values for ${country}, ${indicator}, ${filter}`, () => {
    expect(
      getTradeoffValues(country, indicator, filter, {
        tradeoffData,
        assessmentsData,
        countriesData,
      })
    ).toEqual([numberArrowMap[values[0]]]);
  });
});
