import { loadData } from "helpers/loadData.js";
import {
  extractValues,
  getAllObservations,
  getPotentialValues,
} from "tests/helpers/getData";

const expectedPotentialData = require("tests/expected-results/potential.json");

const totExpectedResults = extractValues(expectedPotentialData);

let potentialData;
let assessmentsData;
let countriesData;

beforeAll(async () => {
  const [{ potential }] = await loadData(["potential"]);
  const [{ assessments }] = await loadData(["assessments"]);
  const [{ countries }] = await loadData(["countries"]);
  potentialData = potential;
  assessmentsData = assessments;
  countriesData = countries;
});

it(`renders all data for the homepage section`, () => {
  expect(getAllObservations(potentialData)).toHaveLength(
    getAllObservations(totExpectedResults).length
  );
});

expectedPotentialData.forEach(({ country, indicator, filter, values }) => {
  it(`has the correct values for ${country}, ${indicator}, ${filter}`, () => {
    expect(
      getPotentialValues(country, indicator, filter, {
        potentialData,
        assessmentsData,
        countriesData,
      })
    ).toEqual(values);
  });
});
