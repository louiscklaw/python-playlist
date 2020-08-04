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
      <Navbar nav_items={page_context.result_category}/>


      <section className={style.section}>

        <div className={style.container}>
          <div className={combineStyle([style.title, style.is4])}>
            {test_suite_name} test
          </div>

          <div>
            <div className={combineStyle([style.title, style.is5])}>
              descriptions:
            </div>

            <div className={combineStyle([style.is6])}>
              <TestDescription content={test_meta} />
            </div>
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