import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import Navbar from '../components/nav'
import SEO from "../components/seo"

import style from '../scss/style.module.scss'

function SmokeTestReport(props){
  return(
    <Layout>

      <SEO title="Smoke test" />
      <Navbar />

      <section className={style.section} style={{
        paddingTop: '1rem', paddingBottom: '1rem'
      }}>
        <div className={style.container}>
          <p className={style.title+' '+style.is4}> Test progress overview </p>
        </div>
      </section>

    </Layout>
  )
}

export default SmokeTestReport
