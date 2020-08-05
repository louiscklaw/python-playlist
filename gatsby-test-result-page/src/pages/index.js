import React from "react"

import { Link, navigate } from "gatsby"

import Navbar from '~components/nav'

import PreJson from '~components/pre-json'
import PreUnittest from '~components/pre-unittest'

import style from '~scss/style.module.scss'
import {combineStyle} from '~utils/common'

function IndexPage() {

  React.useEffect(()=>{
    navigate('/unit')
  },[])


  return (
    <>
      Please enable javascript for page working ...
    </>
  )

}

export default IndexPage
