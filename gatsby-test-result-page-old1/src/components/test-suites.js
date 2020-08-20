import React from 'react'

import Card from './card'

import TestDescription from '~components/test-description'

import style from '~scss/style.module.scss'
import {combineStyle} from '~utils/common'

function TestSuites(props){
  let test_result_reports = props.reports
  let testsuites = test_result_reports.testsuite

  let [test_result_title, setTestResultTitle] = React.useState('')
  let test_result_explain = test_result_reports.explain ? test_result_reports.explain : ''
  let test_result_meta = test_result_reports.meta

  // NOTES:
  // testsuites have only one testsuite inside will return a object without key
  // testsuites have multiple testsuite inside will return a object with "idx (e.g. 0,1,2...)" as key
  let testsuites_array = typeof(testsuites[0])=='undefined' ? {"0": testsuites} : testsuites

  React.useEffect(()=>{
    console.log('test_result_reports.title', test_result_reports.title)
    setTestResultTitle(test_result_reports.title ? test_result_reports.title: '')
  },[test_result_reports])

  return(
    <div>

      {/* container */}
      <div className={style.container}>
        <div className={style.testResultHeader}>
          <div className={combineStyle([style.title, style.is6])}>
            {test_result_title}
          </div>
          <div className={combineStyle([style.subTitle, style.is6])}>
            {test_result_explain}
          </div>
        </div>
      </div>
      {/* container */}


      {/* container */}
      <div className={style.container}>
        <div className={style.testResultHeader}>
          <div className={combineStyle([style.title, style.is6])}>
            Descriptions:
          </div>

          <div className={combineStyle([style.is6])}>
            <TestDescription content={test_result_meta} />
          </div>
        </div>
      </div>
      {/* container */}


      {/* container */}
      <div className={style.container}>
        <div className={style.cardWrapper}>
          {
            Object.keys(testsuites_array)
            .sort()
            .map(idx => <Card {...testsuites_array[idx]} key={`card_${idx}`}/> )
          }
        </div>
      </div>
      {/* container */}

    </div>
  )
}


export default TestSuites