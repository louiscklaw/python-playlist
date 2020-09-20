import React from 'react'
import {Link} from 'gatsby'

import SEO from "../components/seo"

import Layout from "../components/layout"
import Navbar from '../components/nav'
import DoughnutResultCards from '../components/doughnut-result-cards'
import EmptyCard from '../components/empty-card'

import Footer from '../components/footer'
import PageHeadings from '../components/page-headings'

import ThemeContext from '../contexts/ThemeContext'
import ResultContext from '../contexts/ResultContext'

import { combineStyles } from '../../utils/common'

function HelloworldPage(props){
  const {active_style} = React.useContext(ThemeContext)
  const {fetchTestSuiteResult} = React.useContext(ResultContext)

  let [test_suite_result, setTestSuiteResult] = React.useState()

  const getTestSuiteNames = (test_suite_result) => Object.keys(test_suite_result)

  React.useEffect(()=>{
    fetchTestSuiteResult('unit_test')
      .then(r => r.json())
      .then(r_json=> setTestSuiteResult(r_json) )
  },[])

  const getNumberOfTestSuite = (test_suite_results) => Object.keys(test_suite_results).length
  const getNumberOfRow = (total_items, item_per_row) => Math.ceil(total_items / item_per_row)

  const getDoughnutCards = (results) => {
    if (results != null){
      let number_of_row = getNumberOfRow(getNumberOfTestSuite(results), 4)
      let out = Array(number_of_row).fill(1)
      return(
        <>
          {
            out.forEach(x => {

              return(
                <div className={combineStyles([active_style.columns, active_style.isDesktop])}>
                  <DoughnutResultCards card_configs={[
                    {result_to_show: test_suite_result['test_suite_1'], result_name: `unit_test.name`, result_description: `unit_test.description` },
                    {result_to_show: test_suite_result['test_suite_1'], result_name: `integration_test.name`, result_description: `integration_test.description`},
                    {result_to_show: test_suite_result['test_suite_1'], result_name: 'unit test 3', result_description: 'result_description3'},
                    {result_to_show: test_suite_result['test_suite_1'], result_name: 'unit test 4', result_description: 'result_description4'}
                    ]}>


                    </DoughnutResultCards>
                </div>
              )
            })
          }
        </>
      )

    }else{
      return( null )
    }
  }

  return(
    <Layout>
      <SEO title="helloworld page" />
      <Navbar active_nav_item="unit_test" />

      <PageHeadings {...props} />

      <section className={active_style.section}>
        <div className={active_style.container}>

          {
            getDoughnutCards(test_suite_result)
          }


          <div>
            <Link to="/"> Back </Link>
          </div>

        </div>
      </section>

    </Layout>

  )
}

export default HelloworldPage