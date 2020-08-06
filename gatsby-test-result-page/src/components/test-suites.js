import React from 'react'

import Card from './card'

import style from '~scss/style.module.scss'

function TestSuites(props){
  let testsuites = props.reports.testsuite

  // NOTES:
  // testsuites have only one testsuite inside will return a object without key
  // testsuites have multiple testsuite inside will return a object with "idx (e.g. 0,1,2...)" as key
  let testsuites_array = typeof(testsuites[0])=='undefined' ? {"0": testsuites} : testsuites

  return(
    <div className={style.cardWrapper}>
      {
        Object.keys(testsuites_array)
        .sort()
        .map(idx => <Card {...testsuites_array[idx]} key={`card_${idx}`}/> )
      }
    </div>
  )
}


export default TestSuites