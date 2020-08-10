import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import Navbar from '../components/nav'
import SEO from "../components/seo"

import style from '../scss/style.module.scss'

import Card from '../components/card'
import Footer from '../components/footer'

const combineStyle = (styles_in) => styles_in.join(' ')

const OverviewPage = () => (
  <Layout>

    <SEO title="Overview" />
    <Navbar />

    <section className={style.section} style={{
      paddingTop: '1rem', paddingBottom: '1rem'
    }}>
      <div className={style.container}>
        <p className={style.title+' '+style.is4}> Test progress overview </p>
      </div>
    </section>



    <section className={style.section} style={{paddingTop: '0.5rem', fontSize:'small'}}>
      <div className={style.container}>

        <div className={combineStyle([style.columns, style.isDesktop])}>
          {
            [0,1,2,3].map(x => {
              return(
                <div className={style.column}>
                  <Card />
                </div>
              )
            })
          }
        </div>

        <div className={combineStyle([style.columns, style.isDesktop])}>
          {
            [0,1,2].map(x => {
              return(
                <div className={style.column}>
                  <Card />
                </div>
              )
            })
          }

          <div className={style.column}>
            <Card />
          </div>

        </div>

      </div>
    </section>


    <Footer />

  </Layout>
)

export default OverviewPage
