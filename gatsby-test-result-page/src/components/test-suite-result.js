import {
  checkTestPassed,
  checkTestError,
  checkTestSkipped
} from '../utils/common'

import React from 'react'

function ShowError(test_detail){
  return(
    <>
      error_testcase
    </>
  )
}

function ShowSkip(test_detail){
  return(
    <>
      skipped_testcase
    </>
  )
}

function TestSuiteResult(props){
  let test_detail_json = props
  return(
    <>

      <h4>TestSuiteResult</h4>

      <div> {JSON.stringify(Object.keys(test_detail_json))} </div>

      <div> {test_detail_json['@classname']} </div>
      <div> {test_detail_json['@file']} </div>
      <div> {test_detail_json['@line']} </div>
      <div> {test_detail_json['@name']} </div>
      <div> {test_detail_json['@time']} </div>
      <div> {test_detail_json['@timestamp']} </div>
      <div> {test_detail_json['@system-out']} </div>
      <div> {test_detail_json['@system-err']} </div>

      <div> {checkTestPassed(test_detail_json) ? 'test passed':'not pass'} </div>
      <div> { checkTestError(test_detail_json) ? <ShowError />: 'not error' } </div>
      <div> { checkTestSkipped(test_detail_json) ? <ShowSkip />: 'not skipped' } </div>

      <pre>
        {JSON.stringify(test_detail_json, null, 2)}
      </pre>

    </>
  )
}

export default TestSuiteResult