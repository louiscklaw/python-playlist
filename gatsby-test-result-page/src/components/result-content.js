import React from 'react'

import PreJson from '~components/pre-json'
import PreUnittest from '~components/pre-unittest'
import TestSuites from '~components/test-suites'

import GlobalContext from '~contexts/global'

function Loading(){
  return(
    <>
      Loading
    </>
  )
}

function showTestSuite(props){
  return(
    <TestSuites {...props}/>
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
      setTestResultShowHere(showTestSuite(test_type_result_json))
    }else{
      setTestResultShowHere( 'the wanted test type not found'+JSON.stringify({}) )
    }

    console.log(props.test_type)
    console.log(python_test_result[test_type])

  },[python_test_result])


  return(
    <>
      { test_result_show_here }
    </>
  )
}

export default ResultContent
