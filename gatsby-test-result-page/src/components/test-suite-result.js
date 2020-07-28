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

  return(
    <div style={test_results_style}>
      { Object.values(props).map( test_result => <IconStatus {...test_result} /> )}
    </div>
  )

}

export default TestSuiteResult
