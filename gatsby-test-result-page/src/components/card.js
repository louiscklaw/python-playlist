import React from 'react'
import ReactMarkdown from 'react-markdown'


import style from '../scss/style.module.scss'
import IconStatus from './icon-status'

import {combineStyle} from '../utils/common'

function custHeaderStyle(level, props){
  switch (level) {
    case 1:
      console.log(props)
      return (<h1 className={combineStyle([style.title, style.is4])}>{props.children}</h1>)
    case 2:
      console.log(props)
      return (<h2 className={combineStyle([style.subtitle, style.is4])}>{props.children}</h2>)
    case 3:
      console.log(props)
      return (<h3 className={combineStyle([style.title, style.is5])}>{props.children}</h3>)
    case 4:
      console.log(props)
      return (<h4 className={combineStyle([style.subtitle, style.is5])}>{props.children}</h4>)
    case 5:
      console.log(props)
      return (<h5 className={combineStyle([style.title, style.is6])}>{props.children}</h5>)
    case 6:
      console.log(props)
      return (<h6 className={combineStyle([style.subtitle, style.is6])}>{props.children}</h6>)

    default:
      return "hello custHeaderStyle"
      break;
  }
}

function Card(props){
  'card = testsuite'
  let testsuite = props
  let testcases = testsuite.testcase

  let testcases_array = testcases['0'] ? testcases: [testcases]

  let testsuite_classname = testcases['0'] ? testcases['0']['@classname'] : testcases['@classname']
  let testsuite_errors = testsuite['@errors']
  let testsuite_failures = testsuite['@failures']

  let testsuite_name = testsuite['@name'].split('.')[1].split('-')[0]

  let testsuite_tests = testsuite['@tests']
  let testsuite_time = testsuite['@time']

  let card_title = props.title ? props.title : testsuite_classname.split('.')[1]

  return(
    <div className={style.resultCard}>
      <div className={style.card}>
        <header className={style.cardHeader}>
        <h3 className={style.cardHeaderTitle}>{card_title}</h3>
        </header>

        <div className={style.cardContent}>

          {/* result tile */}
          <div className={style.resultTile}>
            <div className={style.resultGridWrapper}>
              {
                testcases_array.map(testcase => <IconStatus {...testcase} key={`icon_status_${JSON.stringify(testcase)}`}/> )
              }
            </div>
          </div>
          {/* result tile */}

          {/* result description */}
          <div className={style.content}>
            <br />
              <ReactMarkdown
                source={props.doc_string}
                escapeHtml={false}
                renderers={{
                  heading: props => custHeaderStyle(props.level, props)
                }}
                />

            <br /><a>{testsuite_name}</a>
            <br /><a>errors: {testsuite_errors}</a>
            <br /><a>failures: {testsuite_failures}</a>.
            <br /><a>tests: {testsuite_tests}</a>
            <br /><a href="#">total time spent: {testsuite_time}</a>
            <br />
          </div>
          {/* result description */}


        </div>


      </div>
    </div>


  )
}

export default Card
