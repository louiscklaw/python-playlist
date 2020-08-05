import React from "react"

import { Link, navigate } from "gatsby"
import Navbar from '../components/navbar'
import PreJson from '../components/pre-json'

import style from '../scss/style.module.scss'
import {combineStyle} from '../utils/common'

function IndexPage() {

  React.useEffect(()=>{
    navigate('/unit')
  },[])


  return (
    <div>
      <Navbar />
      update
      <PreJson />
    </div>
  )

}

export default IndexPage
