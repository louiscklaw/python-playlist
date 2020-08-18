import React from "react"
import { Link } from "gatsby"

import SEO from "../components/seo"

import Layout from "../components/layout"
import Navbar from '../components/nav'
import Cards from '../components/cards'
import Footer from '../components/footer'
import PageHeadings from '../components/page-headings'

import ThemeContext from '../contexts/ThemeContext'

function OverviewPage(props){
  const {active_style} = React.useContext(ThemeContext)
  return(
    <Layout>
      <SEO title="Overview" />
      <Navbar />
      <PageHeadings />
      <section className={active_style.section}>
        <div className={active_style.container}>

          <Cards />


        </div>
      </section>
    </Layout>
  )
}

export default OverviewPage
