import React from 'react'
import {Link} from 'gatsby'
import Navbar from '../components/nav'

import style from '../scss/style.module.scss'
import {combineStyle} from '../utils/common'

import TestSuiteResult from '../components/test-suite-result'

function jsonTemplate(props){
  let page_context = props.pageResources.json.pageContext

  let test_result = page_context.testResult
  let test_suite_name = page_context.testSuiteName

  let test_case = page_context.testcase

  let testsuite = test_result.testsuites

  return(
    <>
      <Navbar />
      <div className={combineStyle([style.title, style['is-6']])}>
        {test_suite_name}
      </div>

      <div>
        <Link to={`/`}>Back</Link>
      </div>

      <h4> pass case </h4>
      <div>
        <TestSuiteResult {...test_case} />
      </div>

      <pre>
        {JSON.stringify(testsuite, null, 2)}
      </pre>

    </>
  )
}


export default jsonTemplate