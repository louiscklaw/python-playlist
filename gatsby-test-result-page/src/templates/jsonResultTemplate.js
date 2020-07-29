import React from 'react'
import {Link} from 'gatsby'
import Navbar from '../components/nav'

import style from '../scss/style.module.scss'
import {combineStyle} from '../utils/common'

import TestDescription from '../components/test-description'

import TestSuite from '../components/test-suite'
import TestSuites from '../components/test-suites'
import TestSuiteResult from '../components/test-suite-result'

// # This is a header

// And this is a paragraph **bold**

// This block of Markdown contains <a href="https://en.wikipedia.org/wiki/HTML">HTML</a>, and will require the <code>html-parser</code> AST plugin to be loaded, in addition to setting the <code class="prop">escapeHtml</code> property to false.

// helloworld

// <custom test="test_props">
// hello code apple aaa
// </custom>

function jsonTemplate(props){
  let page_context = props.pageResources.json.pageContext

  let test_result = page_context.testResult
  let test_reports = test_result.reports
  let test_meta_desc = test_reports.meta.desc
  let test_suite_name = page_context.testSuiteName
  let testsuites = page_context.testResult.reports.testsuite



  return(
    <>
      <Navbar />
      <div className={combineStyle([style.title, style['is-6']])}>
        {test_suite_name} test
      </div>

      <div>
        <Link to={`/`}>Back</Link>
      </div>

      <div>
        descriptions:
        <TestDescription content={`# This is a header`} />
        <pre>
          {JSON.stringify(test_meta_desc, null, 2)}
        </pre>
      </div>

      <div>
        <TestSuites {...testsuites}/>
      </div>

      {/*
        <div>
          <TestSuiteResult {...testsuite[1]} />
        </div>
      */}

    </>
  )
}


export default jsonTemplate