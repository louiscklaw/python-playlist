import React from 'react'

import TestSuite from './test-suite'

function TestSuites(props){
  return(
    <>
      {/* { props.map(test_suite => <TestSuite {...test_suite}/>) } */}
      <pre>
        {JSON.stringify(props[0],null, 2)}
      </pre>
    </>
  )
}

export default TestSuites