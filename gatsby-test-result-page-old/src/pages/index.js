
import React from "react"
import {Link, navigate} from 'gatsby'

import style from '../scss/style.module.scss'

function IndexPage(props){

  React.useEffect(()=>{
    navigate("/content/unit")
  },[])

  return (
    <>
      please click here if page doesn't redirect's you
    </>
  )
}

export default IndexPage
