import React from "react"
import {Link} from 'gatsby'

function IndexPage(props){
  return (
    <div>
      <h1>Sourcing content from YAML</h1>
      <ul>
        <li>
          <Link to="/json-test-result">json-test-result</Link>
        </li>
      </ul>
    </div>
  )
}

export default IndexPage