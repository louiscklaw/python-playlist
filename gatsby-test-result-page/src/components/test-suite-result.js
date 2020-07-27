import React from 'react'

const checkTestPassed = (test_detail) => {
  return (Object.keys(test_detail).indexOf('error') ==-1 && Object.keys(test_detail).indexOf('skipped') ==-1 )
}

function ShowError(test_detail){
  return(
    <>
      error testcase
    </>
  )
}

function ShowSkip(test_detail){
  return(
    <>
      {}
    </>
  )
}

function TestSuiteResult(props){
  return(
    <>

      <h4>TestSuiteResult</h4>

      <div> {JSON.stringify(Object.keys(props))} </div>

      <div> {props['@classname']} </div>
      <div> {props['@file']} </div>
      <div> {props['@line']} </div>
      <div> {props['@name']} </div>
      <div> {props['@time']} </div>
      <div> {props['@timestamp']} </div>
      <div> {props['@system-out']} </div>
      <div> {props['@system-err']} </div>

      <div> {checkTestPassed(props) ? 'test passed':'not pass'} </div>
      <div> { Object.keys(props).indexOf("error") > -1 ? <ShowError />: 'not error' } </div>
      <div> { Object.keys(props).indexOf("skipped") > -1 ? <ShowSkip />: 'not skipped' } </div>

      <pre>
        {JSON.stringify(props, null, 2)}
      </pre>

    </>
  )
}

export default TestSuiteResult