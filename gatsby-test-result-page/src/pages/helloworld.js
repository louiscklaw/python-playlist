import React from 'react'
import {Link} from 'gatsby'

import SEO from "../components/seo"

import Layout from "../components/layout"
import Navbar from '../components/nav'

import Footer from '../components/footer'
import PageHeadings from '../components/page-headings'

import ThemeContext from '../contexts/ThemeContext'
import ResultContext from '../contexts/ResultContext'

function HelloworldPage(props){
  const {active_style} = React.useContext(ThemeContext)

  const {tests_result} = React.useContext(ResultContext)

  return(
    <Layout>
      <SEO title="helloworld page" />
      <Navbar active_nav_item="unit_test" />

      <PageHeadings {...props} />
      <section className={active_style.section}>
        <div className={active_style.container}>

          {JSON.stringify(tests_result)}

          <div>
            <Link to="/"> Back </Link>
          </div>

        </div>
      </section>

    </Layout>

  )
}

export default HelloworldPage