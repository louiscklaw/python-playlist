import React from 'react'

import style from '../scss/style.module.scss'
import IconStatus from './icon-status'

function Card(props){
  'card = testsuite'
  let testcases = props.testcase

  let testsuite_classname = testcases['0']['@classname']
  let testsuite_errors = "0"
  let testsuite_failures = "0"
  let testsuite_name = "TestSuite1-20200729162324"
  let testsuite_tests = "2"
  let testsuite_time = "0.000"

  return(

    <div className={style.card}>
      <header className={style.cardHeader}>
      <h3 className={style.cardHeaderTitle}>{testsuite_classname}</h3>
      </header>

      <div className={style.resultTile}>
        <div className={style.resultGridWrapper}>
          {
            testcases.map(testcase => <IconStatus {...testcase} key={`icon_status_${JSON.stringify(testcase)}`}/> )
          }
        </div>
      </div>

      <div className={style.cardContent}>
        <div className={style.media}>

        </div>
      </div>

      <div className={style.content}>
        <br /><a>{testsuite_name}</a>
        <br /><a>errrors: {testsuite_errors}</a>
        <br /><a>failures: {testsuite_failures}</a>.
        <br /><a>tests: {testsuite_tests}</a>
        <br /><a href="#">total time spent: {testsuite_time}</a>
        <br />
      </div>
    </div>

  )
}

export default Card
