import React from 'react'

import json_fetcher from '../endpoints/json_fetcher'

const default_value ={
  hello:'world',
  getResultByTestName: () => {},
  fetchTestSuiteResult: () => {}
}
const ResultContext = React.createContext(default_value)

function ResultContextProvider(props){
  let {children} = props
  const [hello, setHello] = React.useState(null)
  const [hello_json, setHelloJson] = React.useState(null)

  const [tests_result, setTestsResult] =React.useState(null)
  const [unittest_result, setUnittestResult] = React.useState(null)

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


    json_fetcher.fetchUnitTestResultJson()
      .then(r => r.json())
      .then( r_json=> setUnittestResult(r_json))
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
        getResultByTestName,
        unittest_result
        }}>
        {children}
      </ResultContext.Provider>
    </>
  )
}

export default ResultContext

export {ResultContextProvider}
