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

  const {test_result_to_show} = props

  const [chart_data, setChartData] = React.useState(null)

  const getTestResultToShow = (chart_config, result_data) => {
    // result_data
    return {...chart_config}
  }

  React.useEffect(()=>{
    console.log('card.js',test_result_to_show)
    // console.log('card.js','helloworld')

    let chart_labels = ['passed','failed','error','in_prog']
    let chart_values = chart_labels.map(chart_label => test_result_to_show[chart_label].value)

    console.log('labels',chart_labels)
    console.log('values', chart_values)
    console.log('colors', chart_colors)

    setChartData( {
      labels: chart_labels,
      datasets: [{
        data: chart_values,
        backgroundColor: chart_colors,
        hoverBackgroundColor: [
        '#FF6384',
        '#36A2EB',
        '#FFCE56'
        ]
      }]
    })
  },[chart_config, test_result_to_show])

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
            text: `test_name` + ' result'
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
          Unit test
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
            <td>In progress</td>
            <td>Error</td>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>10</td>
            <td>2</td>
            <td>13</td>
            <td>1</td>
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
