import React from 'react'

import Card from './card'

import ResultContext from '../contexts/ResultContext'
import ThemeContext from '../contexts/ThemeContext'
import { combineStyles } from '../../utils/common'

function Cards(props){
  const {active_style} = React.useContext(ThemeContext)
  const {tests_result} = React.useContext(ResultContext)

  return(
    <div className={combineStyles([active_style.columns, active_style.isDesktop])}>
      <div className={active_style.column}>
        <Card
          test_result_to_show={tests_result.unit_test}
          result_name="unit test1"
          />
      </div>
      <div className={active_style.column}>
        <Card
          test_result_to_show={tests_result.unit_test}
          result_name="unit test2"
        />
      </div>
      <div className={active_style.column}>
        <Card
          test_result_to_show={tests_result.unit_test}
          result_name="unit test3"
        />
      </div>
      <div className={active_style.column}>
        <Card
          test_result_to_show={tests_result.unit_test}
          result_name="unit test4"
        />
      </div>
    </div>
  )
}

export default Cards