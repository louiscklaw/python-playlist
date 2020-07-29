import React from 'react'

import style from '../scss/style.module.scss'
import IconStatus from './icon-status'

function Card(props){
  'card = testsuite'
  let testcases = props.testcase

  let testsuite_name = testcases['0']['@classname']

  return(

    <div className={style.card}>
      <header className={style.cardHeader}>
      <h3 className={style.cardHeaderTitle}>{testsuite_name}</h3>
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
        testing the outlook of the page
        <br /><a>@bulmaio</a>.
        <br /><a href="#">#css</a>
        <br /><a href="#">#responsive</a>
        <br />
        <time dateTime="2016-1-1">11:09 PM - 1 Jan 2016</time>
      </div>
    </div>

  )
}

export default Card
