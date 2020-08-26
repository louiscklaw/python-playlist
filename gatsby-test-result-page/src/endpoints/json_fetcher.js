
const fetchHelloJson = () => fetch('/json/hello.json')
const fetchTestsResultJson = () => fetch('/json/tests_result.json')

const fetchTestSuiteResultJson = (test_suite_name) => fetch(`/json/${test_suite_name}.json`)

export default {
  fetchHelloJson,
  fetchTestsResultJson,
  fetchTestSuiteResultJson
}
