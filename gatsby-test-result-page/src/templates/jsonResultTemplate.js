import React from 'react'
import {Link} from 'gatsby'
import Navbar from '../components/nav'

import style from '../scss/style.module.scss'
import {combineStyle} from '../utils/common'

import TestDescription from '../components/test-description'

import TestSuite from '../components/test-suite'
import TestSuites from '../components/test-suites'
import TestSuiteResult from '../components/test-suite-result'

function jsonTemplate(props){
  let page_context = props.pageResources.json.pageContext

  let test_result = page_context.testResult
  let test_reports = test_result.reports
  let test_meta = test_reports.meta
  let test_suite_name = page_context.testSuiteName
  let testsuites = page_context.testResult.reports.testsuite



  return(
    <>
      <Navbar />


      <section className={style.section}>

        <div className={style.container}>
          <div className={combineStyle([style.title, style['is-6']])}>
            {test_suite_name} test <Link to={`/`}>Back</Link>
          </div>

          <div>
            descriptions:
            <TestDescription content={test_meta} />
          </div>

          <div>
            <TestSuites {...testsuites}/>
          </div>

        </div>


      </section>

      {/*
        <div>
          <TestSuiteResult {...testsuite[1]} />
        </div>
      */}

    </>
  )
}


export default jsonTemplate