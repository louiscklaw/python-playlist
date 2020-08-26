import React from 'react'

import json_fetcher from '../endpoints/json_fetcher'

const default_value ={
  hello:'world',
  getResultByTestName: () => {},
  fetchTestSuiteResult: () => {}
}
const ResultContext = React.createContext(default_value)

// const tests_result1={
//   unit_test: {
//     failed: {
//       value: 1
//     },
//     in_prog: {
//       value: 2
//     },
//     error: {
//       value: 3
//     },
//     passed: {
//       value: 4
//     },
//     run_time: '10',
//     test_description: ' UNIT TESTING is a level of software testing where individual units/ components of a software are tested.'
//   },
//   integration_test: {
//     failed: {
//       value: 5
//     },
//     in_prog: {
//       value: 6
//     },
//     error: {
//       value: 7
//     },
//     passed: {
//       value: 8
//     },
//     run_time: '10',
//     test_description: ' UNIT TESTING is a level of software testing where individual units/ components of a software are tested.'
//   },
//   acceptance_test: {
//     failed: {
//       value: 1
//     },
//     in_prog: {
//       value: 1
//     },
//     error: {
//       value: 1
//     },
//     passed: {
//       value: 10
//     },
//     run_time: '10',
//     test_description: ' UNIT TESTING is a level of software testing where individual units/ components of a software are tested.'
//   },
//   interface_test: {
//     failed: {
//       value: 1
//     },
//     in_prog: {
//       value: 1
//     },
//     error: {
//       value: 1
//     },
//     passed: {
//       value: 1
//     },
//     run_time: '10',
//     test_description: ' UNIT TESTING is a level of software testing where individual units/ components of a software are tested.'
//   },
//   regression_test: {
//     failed: {
//       value: 1
//     },
//     in_prog: {
//       value: 1
//     },
//     error: {
//       value: 1
//     },
//     passed: {
//       value: 1
//     },
//     run_time: '10',
//     test_description: ' UNIT TESTING is a level of software testing where individual units/ components of a software are tested.'
//   },
//   sanity_test: {
//     failed: {
//       value: 1
//     },
//     in_prog: {
//       value: 1
//     },
//     error: {
//       value: 1
//     },
//     passed: {
//       value: 1
//     },
//     run_time: '10',
//     test_description: ' UNIT TESTING is a level of software testing where individual units/ components of a software are tested.'
//   },
//   smoke_test: {
//     failed: {
//       value: 1
//     },
//     in_prog: {
//       value: 1
//     },
//     error: {
//       value: 1
//     },
//     passed: {
//       value: 1
//     },
//     run_time: '10',
//     test_description: ' UNIT TESTING is a level of software testing where individual units/ components of a software are tested.'
//   }
// }

function ResultContextProvider(props){
  let {children} = props
  const [hello, setHello] = React.useState(null)
  const [hello_json, setHelloJson] = React.useState(null)
  const [tests_result, setTestsResult] =React.useState(null)

  const getResultByTestName = (test_name) => {
    let test_result = tests_result[test_name]
    return {
      ...test_result,
      name: test_name,
      description: test_result.test_description
    }
  }

  React.useEffect(()=>{
    // json_fetcher.fetchHelloJson()
    //   .then(r => r.json())
    //   .then(r_json=> setHelloJson(r_json))

    json_fetcher.fetchTestsResultJson()
      .then(r => r.json())
      .then(r_json => setTestsResult(r_json))

  },[])

  const fetchTestSuiteResult = (test_suite_name) => {
    return json_fetcher.fetchTestSuiteResultJson(test_suite_name)
  }

  return(
    <>
      <ResultContext.Provider value={{
        hello, setHello,
        tests_result,
        hello_json, fetchTestSuiteResult,
        getResultByTestName
        }}>
        {children}
      </ResultContext.Provider>
    </>
  )
}

export default ResultContext

export {ResultContextProvider}
