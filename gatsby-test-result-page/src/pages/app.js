import React from "react"
import {Link} from 'gatsby'

import { Router } from "@reach/router"

import Layout from "../components/layout"
import Navbar from '~components/nav'
import ResultContent from '~components/result-content'

import style from '~scss/style.module.scss'
import {combineStyle} from '~utils/common'

const App = () => {
  return (
    <Layout>
      <section className={style.section} >
        <Router basepath="/">
          <ResultContent path="/content/:test_type" />
        </Router>
      </section>
    </Layout>
  )
}

export default App