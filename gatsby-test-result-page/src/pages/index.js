import React from "react"

import { Link, navigate } from "gatsby"

import { Router } from "@reach/router"
import ResultContent from '~components/result-content'

import Navbar from '~components/nav'

import PreJson from '~components/pre-json'
import PreUnittest from '~components/pre-unittest'

import style from '~scss/style.module.scss'
import {combineStyle} from '~utils/common'

function IndexPage() {

  React.useEffect(()=>{
    navigate('content/unit_test')
  },[])

  return (
    <>
      index.js
      <Link to="/app">app page</Link>
    </>
  )

}

export default IndexPage
