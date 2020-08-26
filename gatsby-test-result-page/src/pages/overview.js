import React from "react"
import { Link } from "gatsby"

import SEO from "../components/seo"

import Layout from "../components/layout"
import Navbar from '../components/nav'
import DoughnutResultCards from '../components/doughnut-result-cards'
import EmptyCard from '../components/empty-card'

// import Cards from '../components/cards'
import Footer from '../components/footer'
import PageHeadings from '../components/page-headings'

import ResultContext from '../contexts/ResultContext'
import ThemeContext from '../contexts/ThemeContext'

import { combineStyles, chunkArray } from '../../utils/common'
import DoughnutTimeSpentCard from "../components/doughnut-timespent-card"

function fillToTheMultipliesOfRow(array_in, number_per_row){
  return 'helloworld'
}

function OverviewPage(props){
  const {active_style} = React.useContext(ThemeContext)
  const {tests_result, getResultByTestName} = React.useContext(ResultContext)

  // let unit_test = tests_result.unit_test
  let unit_test = getResultByTestName('unit_test')
  let integration_test = getResultByTestName('integration_test')


  let test_results_list = [
    unit_test,
    integration_test,
    integration_test,
    integration_test,
    integration_test,
    null,
    null,
    null
  ]

  let number_of_card_per_row = 4

  return(
    <Layout>
      <SEO title="Overview" />

      <Navbar active_nav_item="overview" />

      <PageHeadings {...props} />
      <section className={active_style.section}>

        {/* container */}
        <div className={active_style.container}>
          <h2 className={combineStyles([active_style.title, active_style.is4])} style={{textDecoration:"underline"}}>Test results</h2>

          {
            chunkArray(test_results_list, number_of_card_per_row).map( chunk =>{
              return(
                <div className={combineStyles([active_style.columns, active_style.isDesktop])}>
                  {
                    chunk.map( repo_name => {
                      if (repo_name ==null){
                        return(
                          <div className={active_style.column}>
                          </div>
                        )
                      }else{
                        return(
                          <div className={active_style.column}>
                            {JSON.stringify(repo_name)}
                          </div>
                        )
                      }
                    })
                  }
                </div>
              )
            })
          }

          <div className={combineStyles([active_style.columns, active_style.isDesktop])}>
            <DoughnutResultCards card_configs={[
              {result_to_show: unit_test, result_name: unit_test.name, result_description: unit_test.description },
              {result_to_show: integration_test, result_name: integration_test.name, result_description: integration_test.description},
              {result_to_show: tests_result.acceptance_test, result_name: 'unit test 3', result_description: 'result_description3'},
              {result_to_show: tests_result.interface_test, result_name: 'unit test 4', result_description: 'result_description4'}
            ]}/>
          </div>

          <div className={combineStyles([active_style.columns, active_style.isDesktop])}>
            <DoughnutResultCards card_configs={[
              {result_to_show: tests_result.regression_test, result_name: 'unit test 1', result_description: 'result_description1'},
              {result_to_show: tests_result.sanity_test, result_name: 'unit test 2', result_description: 'result_description2'},
              {result_to_show: tests_result.smoke_test, result_name: 'unit test 3', result_description: 'result_description3'},
            ]}/>
            <EmptyCard test_result_to_show={null} result_name={null}/>
          </div>


        </div>
        {/* container */}
      </section>

      <section className={active_style.section}>
        <div className={active_style.container}>
          <h2 className={combineStyles([active_style.title, active_style.is4])} style={{textDecoration:"underline"}}>Time spent</h2>

          <div className={combineStyles([active_style.columns, active_style.isDesktop])}>
            <DoughnutResultCards card_configs={[
              {result_to_show: unit_test, result_name: unit_test.name, result_description: unit_test.description },
              {result_to_show: integration_test, result_name: integration_test.name, result_description: integration_test.description},
              {result_to_show: tests_result.acceptance_test, result_name: 'unit test 3', result_description: 'result_description3'},
              {result_to_show: tests_result.interface_test, result_name: 'unit test 4', result_description: 'result_description4'}
            ]}/>
          </div>

          <div className={combineStyles([active_style.columns, active_style.isDesktop])}>
            <DoughnutResultCards card_configs={[
              {result_to_show: tests_result.regression_test, result_name: 'unit test 1', result_description: 'result_description1'},
              {result_to_show: tests_result.sanity_test, result_name: 'unit test 2', result_description: 'result_description2'},
              {result_to_show: tests_result.smoke_test, result_name: 'unit test 3', result_description: 'result_description3'},
            ]}/>
            <EmptyCard test_result_to_show={null} result_name={null}/>
          </div>


        </div>

      </section>
    </Layout>
  )
}

export default OverviewPage
