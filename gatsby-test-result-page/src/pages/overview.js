import React from "react"
import { Link } from "gatsby"

import SEO from "../components/seo"

import Layout from "../components/layout"
import Navbar from '../components/nav'
import Card from '../components/card'
import Footer from '../components/footer'
import PageHeadings from '../components/page-headings'

const OverviewPage = () => (
  <Layout>

    <SEO title="Overview" />
    <Navbar />
    <PageHeadings />

  </Layout>
)

export default OverviewPage
