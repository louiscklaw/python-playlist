import React from "react"
import {Link} from 'gatsby'

import style from '../scss/style.module.scss'
import Navbar from "../components/nav"

import unittest_result_json from '../../content/unit.json'

function HelloworldPage(props){
  return(
    <>
      helloworld page
      <pre>
        {
          JSON.stringify(unittest_result_json, null, 2)
        }
      </pre>
    </>
  )
}


export default HelloworldPage
