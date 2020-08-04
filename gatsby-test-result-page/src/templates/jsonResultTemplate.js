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

  let test_result_reports = test_result.reports

  let test_result_title = test_result_reports.title ? test_result_reports.title: ''
  let test_result_explain = test_result_reports.explain ? test_result_reports.explain : ''
  let test_result_meta = test_result_reports.meta

  let test_suite_name = page_context.testSuiteName
  let testsuites = page_context.testResult.reports.testsuite

  return(
    <>
      {/* <Navbar nav_items={page_context.result_category}/> */}
      <Navbar nav_items={page_context.test_types}/>

      <section className={style.section, style.appendReportSection}>

        <div className={style.container}>
          <div className={combineStyle([style.title, style.is4])}>
            {test_result_title}
          </div>
          <div className={combineStyle([style.subTitle, style.is4])}>
            {test_result_explain}
          </div>
        </div>
      </section>

      <section className={style.section}>
        <div className={style.container}>
          <div className={combineStyle([style.title, style.is5])}>
            Descriptions:
          </div>
          <div className={combineStyle([style.is6])}>
            <TestDescription content={test_result_meta} />
          </div>
        </div>
      </section>

      <section className={style.section}>

        <div className={style.container}>
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
