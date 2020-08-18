import React from 'react'

const default_value ={
  hello:'world'
}
const ResultContext = React.createContext(default_value)

const tests_result={
  unit_test: {
    failed: {
      value: 1
    },
    in_prog: {
      value: 2
    },
    error: {
      value: 3
    },
    passed: {
      value: 4
    },
    run_time: '10',
    test_description: ' UNIT TESTING is a level of software testing where individual units/ components of a software are tested.'
  },
  integration_test: {
    failed: {
      value: 5
    },
    in_prog: {
      value: 6
    },
    error: {
      value: 7
    },
    passed: {
      value: 8
    },
    run_time: '10',
    test_description: ' UNIT TESTING is a level of software testing where individual units/ components of a software are tested.'
  },
  acceptance_test: {
    failed: {
      value: 1
    },
    in_prog: {
      value: 1
    },
    error: {
      value: 1
    },
    passed: {
      value: 10
    },
    run_time: '10',
    test_description: ' UNIT TESTING is a level of software testing where individual units/ components of a software are tested.'
  },
  interface_test: {
    failed: {
      value: 1
    },
    in_prog: {
      value: 1
    },
    error: {
      value: 1
    },
    passed: {
      value: 1
    },
    run_time: '10',
    test_description: ' UNIT TESTING is a level of software testing where individual units/ components of a software are tested.'
  },
  regression_test: {
    failed: {
      value: 1
    },
    in_prog: {
      value: 1
    },
    error: {
      value: 1
    },
    passed: {
      value: 1
    },
    run_time: '10',
    test_description: ' UNIT TESTING is a level of software testing where individual units/ components of a software are tested.'
  },
  sanity_test: {
    failed: {
      value: 1
    },
    in_prog: {
      value: 1
    },
    error: {
      value: 1
    },
    passed: {
      value: 1
    },
    run_time: '10',
    test_description: ' UNIT TESTING is a level of software testing where individual units/ components of a software are tested.'
  },
  smoke_test: {
    failed: {
      value: 1
    },
    in_prog: {
      value: 1
    },
    error: {
      value: 1
    },
    passed: {
      value: 1
    },
    run_time: '10',
    test_description: ' UNIT TESTING is a level of software testing where individual units/ components of a software are tested.'
  }
}

function ResultContextProvider(props){
  let {children} = props
  const [hello, setHello] = React.useState(null)

  return(
    <>
      <ResultContext.Provider value={{
        hello, setHello,
        tests_result
      }}>
        {children}
      </ResultContext.Provider>
    </>
  )
}

export default ResultContext

export {ResultContextProvider}
