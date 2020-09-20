import React from "react"
import { Link } from "gatsby"

import SEO from "../components/seo"

import Layout from "../components/layout"
import Navbar from '../components/nav'

import ThemeContext from '../contexts/ThemeContext'
import { combineStyle } from "../../utils/common"

function WIPPage(props){
  const {active_style, rotateStyle} = React.useContext(ThemeContext)

  return(
    <Layout>
      <SEO title="Overview" />
      <Navbar active_nav_item="overview" />
      <section className={active_style.section}>
        <div className={active_style.container} >
        <div style={{
          width: '100%',
          minHeight: '55vh',
          // backgroundColor: 'grey',

          display: 'flex',
          flexFlow: 'column',
          justifyContent: 'center',
          alignContent: 'center',
          textAlign: 'center'

        }}>
          <div></div>
          <div>
            <h1 className={combineStyle([active_style.title, active_style['is-1']])}>
              Work in progress
            </h1>
          </div>
          <div>
            <div style={{paddingTop: '30px'}}></div>
            <Link to='/overview'>
              back to overview
            </Link>
          </div>
          <div></div>

        </div>

        </div>
      </section>
    </Layout>
  )
}


export default WIPPage