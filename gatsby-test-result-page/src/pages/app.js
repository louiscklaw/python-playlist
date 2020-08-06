import React from "react"
import {Link} from 'gatsby'

import { Router } from "@reach/router"

import Layout from "../components/layout"
import Navbar from '~components/nav'
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