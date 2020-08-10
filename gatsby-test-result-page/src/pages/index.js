import React from "react"
import { Link, navigate } from "gatsby"

import Layout from "../components/layout"
import Navbar from '../components/nav'
import Cards from '../components/cards'

import SEO from "../components/seo"

import style from '../scss/style.module.scss'

function IndexPage (){
  React.useEffect(()=>{
    navigate('/overview')
  })
  return (
    <Layout>
      <SEO title="Index" />
    </Layout>
  )

}
export default IndexPage
