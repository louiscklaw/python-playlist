import React from 'react'
import {Link} from 'gatsby'

import TestSuiteResult from '../components/test-suite-result'

function jsonTemplate(props){
  let test_results = props.pageResources.json.pageContext.testResult
  let test_suite = test_results.testsuite

  let testcases = test_suite.testcase

  return(
    <>
      <div>
        <Link to={`/`}>Back</Link>
      </div>

      <div>
        json template
      </div>

      <h4> pass case </h4>
      <div>
        <TestSuiteResult {...testcases[0]} />
      </div>

      <h4> error case </h4>
      <div>
        <TestSuiteResult {...testcases[2]} />
      </div>

      <h4> skip case </h4>
      <div>
        <TestSuiteResult {...testcases[3]} />
      </div>

    </>
  )
}


export default jsonTemplate