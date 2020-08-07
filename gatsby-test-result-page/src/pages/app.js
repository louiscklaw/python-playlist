import React from "react"

import { Router } from "@reach/router"

import Layout from "../components/layout"
import ResultContent from '~components/result-content'

const App = () => {
  return (
    <Layout>
      <Router basepath="/">
        <ResultContent path="/content/:test_type" />
      </Router>
    </Layout>
  )
}

export default App