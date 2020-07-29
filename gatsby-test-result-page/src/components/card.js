import React from 'react'

import style from '../scss/style.module.scss'
import IconStatus from './icon-status'

function Card(props){
  'card = testsuite'
  let testsuite = props
  let testcases = testsuite.testcase

  let testcases_array = testcases['0'] ? testcases: [testcases]

  let testsuite_classname = testcases['0'] ? testcases['0']['@classname'] : testcases['@classname']
  let testsuite_errors = testsuite['@errors']
  let testsuite_failures = testsuite['@failures']
  let testsuite_name = testsuite['@name']
  let testsuite_tests = testsuite['@tests']
  let testsuite_time = testsuite['@time']



  return(

    <div className={style.card}>
      <header className={style.cardHeader}>
      <h3 className={style.cardHeaderTitle}>{testsuite_classname}</h3>
      </header>

      <div className={style.resultTile}>
        <div className={style.resultGridWrapper}>
          {
            testcases_array.map(testcase => <IconStatus {...testcase} key={`icon_status_${JSON.stringify(testcase)}`}/> )
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
