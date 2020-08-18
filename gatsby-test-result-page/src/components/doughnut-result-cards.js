import React from 'react'

import DoughnutResultCard from './doughnut-result-card'

import ResultContext from '../contexts/ResultContext'
import ThemeContext from '../contexts/ThemeContext'
import { combineStyles } from '../../utils/common'

function DoughnutResultCards(props){
  const {active_style} = React.useContext(ThemeContext)

  const {card_configs} = props

  return(

    <>
      {
        card_configs.map( ({result_to_show, result_name, result_description}) => {
          return (
            <div className={active_style.column}>
              <DoughnutResultCard
                test_result_to_show={result_to_show}
                result_name={result_name}
                test_description_unit_test={result_description}
                />
            </div>
          )
        })
      }
    </>

  )
}

export default DoughnutResultCards