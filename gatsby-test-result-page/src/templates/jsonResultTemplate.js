import React from 'react'
import {Link} from 'gatsby'
import Navbar from '../components/nav'

import TestSuiteResult from '../components/test-suite-result'

function jsonTemplate(props){
  let test_results = props.pageResources.json.pageContext.testResult
  let test_suite = test_results.testsuite

  let testcase_results = test_suite.testcase

  return(
    <>
      <Navbar />
      <div>
        <Link to={`/`}>Back</Link>
      </div>

      <div> json template </div>

      <h4> pass case </h4>
      <div>
        <TestSuiteResult {...testcase_results} />
      </div>

    </>
  )
}


export default jsonTemplate