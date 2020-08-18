import React from "react"
import { Link } from "gatsby"

import SEO from "../components/seo"

import Layout from "../components/layout"
import Navbar from '../components/nav'
import DoughnutResultCards from '../components/doughnut-result-cards'
// import Cards from '../components/cards'
import Footer from '../components/footer'
import PageHeadings from '../components/page-headings'

import ResultContext from '../contexts/ResultContext'
import ThemeContext from '../contexts/ThemeContext'

import { combineStyles } from '../../utils/common'

function OverviewPage(props){
  const {active_style} = React.useContext(ThemeContext)
  const {tests_result} = React.useContext(ResultContext)

  return(
    <Layout>
      <SEO title="Overview" />
      <Navbar />
      <PageHeadings />
      <section className={active_style.section}>
        <div className={active_style.container}>

          <div className={combineStyles([active_style.columns, active_style.isDesktop])}>
            <DoughnutResultCards card_configs={[
              {result_to_show: tests_result.unit_test, result_name: 'unit test 1'},
              {result_to_show: tests_result.unit_test, result_name: 'unit test 2'},
              {result_to_show: tests_result.unit_test, result_name: 'unit test 3'},
              {result_to_show: tests_result.unit_test, result_name: 'unit test 4'}
            ]}/>
          </div>

          <div className={combineStyles([active_style.columns, active_style.isDesktop])}>
            <DoughnutResultCards card_configs={[
              {result_to_show: tests_result.unit_test, result_name: 'unit test 1'},
              {result_to_show: tests_result.unit_test, result_name: 'unit test 2'},
              {result_to_show: tests_result.unit_test, result_name: 'unit test 3'},
              {result_to_show: tests_result.unit_test, result_name: 'total time spent analysis'}
            ]}/>
          </div>

        </div>
      </section>
    </Layout>
  )
}

export default OverviewPage
