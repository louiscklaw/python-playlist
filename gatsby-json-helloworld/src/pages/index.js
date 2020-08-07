import React from "react"
import { Link } from "gatsby"

import unittest_result_json from '../../content/unit.json'
import not_exist_json from '../../content/not_exist.json'

const IndexPage = () => (
  <>
    helloworld
    <pre>
      {JSON.stringify(unittest_result_json, null , 2)}
    </pre>
  </>
)

export default IndexPage
