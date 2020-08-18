import React from 'react'
import {Doughnut} from 'react-chartjs-2';

import {combineStyles} from '../../utils/common'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {
  faGithub,
  faBug,
  faPalette,
  faQuestionCircle,
  faRoad,
  faCodeBranch,
  faClock,
  faBook,
  faPaste
} from '@fortawesome/free-brands-svg-icons'

import ResultContext from '../contexts/ResultContext'
import ThemeContext from '../contexts/ThemeContext'
import ConfigContext from '../contexts/ConfigContext'
import { object } from 'prop-types';

function ResultCard(props){
  const {active_style} = React.useContext(ThemeContext)

  const {chart_config, chart_colors} = React.useContext(ConfigContext)

  const {test_result_to_show, result_name} = props

  const [chart_data, setChartData] = React.useState({
    passed: 4,
    failed: 1,
    error: 3,
    in_prog: 2
  })
  const [chart_values, setChartValues] = React.useState([])
  const [table_chart_values, setTableChartValues] = React.useState([])

  const getTestResultToShow = (chart_config, result_data) => {
    // result_data
    return {...chart_config}
  }

  React.useEffect(()=>{
    console.log('card.js',test_result_to_show)
    // console.log('card.js','helloworld')

    let chart_labels = ['passed','failed','error','in_prog']

    setTableChartValues({
      passed: test_result_to_show['passed'].value,
      failed: test_result_to_show['failed'].value,
      error: test_result_to_show['error'].value,
      in_prog: test_result_to_show['in_prog'].value
    })

    console.log('chart_labels',chart_labels)
    console.log('test_result_to_show', test_result_to_show.passed)
    console.log('chart_values', chart_values)
    console.log('chart_colors', chart_colors)

    setChartData( {
      labels: chart_labels,
      datasets: [{
        data: [4,1,3,2],
        backgroundColor: chart_colors,
        hoverBackgroundColor: [
        '#FF6384',
        '#36A2EB',
        '#FFCE56'
        ]
      }]
    })
  },[])

  return(
    <>
      {/* card */}
<div className={active_style.card}>
  <div className={active_style.cardImage}>
    <figure className={active_style.is4by3} style={{textAlign: 'center'}}>
      <div id="canvas-holder" style={{width: '90%', margin: 'auto'}}>
        <Doughnut data={chart_data} options={{
          title: {
            display: true,
            text: result_name + ' result'
          },
          aspectRatio: 1,
          responsive: true,
          legend: {
            position: 'right',
          },
          animation: {
            animateScale: true,
            animateRotate: true
          }
        }}/>
      </div>
    </figure>
  </div>
  <div className={active_style.cardContent}>
    <div className={active_style.media}>
      <div className={active_style.mediaContent}>
        <p className={combineStyles([active_style.title, active_style.is4])}>
          {result_name}
          <FontAwesomeIcon icon={faPaste} />
        </p>
      </div>
    </div>
    <div className={active_style.content}>
      <p className={active_style.test_description_unit_test} />
      <table>
        <thead>
          <tr>
            <td>Passed</td>
            <td>Failed</td>
            <td>Error</td>
            <td>In progress</td>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{table_chart_values.passed}</td>
            <td>{table_chart_values.failed}</td>
            <td>{table_chart_values.error}</td>
            <td>{table_chart_values.in_prog}</td>
          </tr>
        </tbody>
      </table>
      <p>time spent: 1hr30min</p>
    </div>
  </div>
</div>
{/* card */}

    </>
  )
}

export default ResultCard
