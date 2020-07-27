import React from "react"
import {Link} from 'gatsby'

import JSONData from "../../content/test-result.json"

const JSONbuildtime = () => (
  <div style={{ maxWidth: `960px`, margin: `1.45rem` }}>
    <pre>
      {JSON.stringify(JSONData, null , 2)}
    </pre>
    <Link to='/'>Back</Link>
  </div>
)
export default JSONbuildtime
