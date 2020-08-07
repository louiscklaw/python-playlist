import React from 'react'

import TestSuites from '~components/test-suites'
import Navbar from '~components/nav'

import style from '~scss/style.module.scss'

import GlobalContext from '~contexts/global'

function Loading(){
  return(
    <>
      Loading
    </>
  )
}

function showTestSuite(result_json, props){
  return(
    <TestSuites {...result_json} {...props} />
  )
}

function ResultContent(props){
  let {python_test_result} = React.useContext(GlobalContext)
  let [test_result_show_here, setTestResultShowHere] = React.useState(null)

  React.useEffect(()=>{
    setTestResultShowHere(Loading())
  },[])

  React.useEffect(()=>{
    let test_type = props.test_type
    let test_type_in_report = test_type
    let test_type_found = Object.keys(python_test_result).indexOf(test_type_in_report) > -1

    if (test_type_found){
      // grep the specific result by test type
      let test_type_result_json = python_test_result[test_type_in_report]
      setTestResultShowHere(showTestSuite(test_type_result_json, props))
    }else{
      setTestResultShowHere( 'the wanted test type not found'+JSON.stringify({}) )
    }

    console.log(props.test_type)
    console.log(python_test_result[test_type])

  },[python_test_result, props.test_type])


  return(
    <>
      <Navbar active_test_type={props.test_type} />
      <section className={style.section} >
        { test_result_show_here }
      </section>
    </>
  )
}

export default ResultContent
