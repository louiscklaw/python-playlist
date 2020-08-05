import {
  checkTestPassed,
  checkTestError,
  checkTestSkipped
} from '../utils/common'

import React from 'react'
import IconStatus from './icon-status'

function TestSuiteResult(props){
  let test_detail_json = props
  console.log([...Object.values(props)])

  const test_results_style = {
    display: 'inline-flex',
  }

  let testcase = props.testcase

  return(
    <div style={test_results_style}>
      { Object.values(testcase).map( test_result => {
        return(
          <IconStatus {...test_result} />
        )
      } )}
    </div>
  )

}

export default TestSuiteResult
