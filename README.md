# Testing utils - JEST

## how to update tests (./tests)

The methodology applied here relies on replicating the backend but with a different programming language. Once that's done, we compare the resulting json files from both the back end and the expected results from running our python code. This method allows us to test ALL observations under seconds. What's time consuming is preparing all tests (max 30 minutes approx for the most time consuming). To update all tests, please refer to the following steps:

- Open one excel file that will be located here -> ./tests/source

- Open the excel file with the updated data. Copy from the updated file and paste to the testing excel file only the data from the tab with the updated data corresponding to the testing section (i.e., potential, tradeoff or homepage).

- Go to the tab named "README", and follow the instructions in there.

- Once you have completed this process for all the testing excel files, then use the script `npm run prepare test` followed by the command `npm run test`
