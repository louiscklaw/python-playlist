import React from "react"

import { Router } from "@reach/router"

import Layout from "../components/layout"
import ResultContent from '~components/result-content'

const App = () => {
  return (
    <Layout>
      <Router basepath="/">
        <ResultContent path="/content/:test_type" />
        <ResultContent path="/content/:test_type/:report_version" />
      </Router>
    </Layout>
  )
}

export default App