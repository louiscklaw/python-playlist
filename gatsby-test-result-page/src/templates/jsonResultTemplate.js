import React from 'react'
import {Link} from 'gatsby'
import Navbar from '../components/nav'

import {combineStylle} from '../utils/common'

import TestSuiteResult from '../components/test-suite-result'

function jsonTemplate(props){
  let test_results = props.pageResources.json.pageContext.testResult
  let test_suite = test_results.testsuite

  let testcase_results = test_suite.testcase

  return(
    <>
      <Navbar />
      <div className={combineStylle([style.title, style['is-6']])}>
        {props.testSuiteName}
      </div>

      <div>
        <Link to={`/`}>Back</Link>
      </div>

      <pre>
        {JSON.stringify(props, null, 2)}
      </pre>

      <div> json template </div>

      <h4> pass case </h4>
      <div>
        <TestSuiteResult {...testcase_results} />
      </div>

    </>
  )
}


export default jsonTemplate