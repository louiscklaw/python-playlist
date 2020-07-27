import React from "react"
import {Link} from 'gatsby'

const IndexPage = () => (
  <div>
    <h1>Sourcing content from YAML</h1>
    <ul>
      <li>
        <Link to="/json-at-buildtime">json-at-buildtime</Link>
      </li>
      <li>
        <Link to="/json-test-result">json-test-result</Link>
      </li>
      <li>
        <Link to="/yml-at-buildtime">yml-at-buildtime</Link>
      </li>
    </ul>
  </div>
)

export default IndexPage
