import {
  checkTestPassed,
  checkTestError,
  checkTestSkipped,
  combineStyle
} from '../utils/common'

import React from 'react'
import IconStatus from './icon-status'

import ResultCard from '../components/result-card'

import style from '../scss/style.module.scss'

function TestSuite(props){
  const test_results_style = {
    display: 'inline-flex',
  }

  let testcase = props.testcase

  return(
    <>
      <ResultCard />

      <p className={combineStyle([style.title, style['is-6']])}>{props['@name']}</p>
      <div style={test_results_style}>
        { Object.values(testcase).map( test_result => {
          return(
            <IconStatus {...test_result} />
          )
        } )}
      </div>

      <pre>
        {JSON.stringify(props, null, 2)}
      </pre>

    </>
  )
}


export default TestSuite