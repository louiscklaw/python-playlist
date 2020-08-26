
const fetchHelloJson = () => fetch('/json/hello.json')
const fetchTestsResultJson = () => fetch('/json/tests_result.json')

const fetchUnitTestResultJson = () => fetch('/json/unit_test_result.json')

const fetchTestSuiteResultJson = (test_suite_name) => fetch(`/json/${test_suite_name}.json`)

export default {
  fetchHelloJson,
  fetchTestsResultJson,
  fetchTestSuiteResultJson,
  fetchUnitTestResultJson
}
