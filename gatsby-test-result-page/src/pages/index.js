import React from "react"
import {Link} from 'gatsby'

import style from '../scss/style.module.scss'
import Navbar from "../components/nav"

function IndexPage(props){
  return (
    <>
      <Navbar />
      <h1>Sourcing content from YAML</h1>
      <ul>
        <li>
          <Link to="/json-test-result">json-test-result</Link>
        </li>
      </ul>
    </>
  )
}

export default IndexPage
