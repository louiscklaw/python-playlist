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

import { combineStyles, chunkArray, fillToTheNearestRow } from '../../utils/common'
import DoughnutTimeSpentCard from "../components/doughnut-timespent-card"
import DoughnutResultCard from '../components/doughnut-result-card'

import json_fetcher from '../endpoints/json_fetcher'

function OverviewPage(props){
  const {active_style} = React.useContext(ThemeContext)
  const {getResultByTestName} = React.useContext(ResultContext)

  let [show_test_result_list, setShowTestResultList] = React.useState([])

  let test_card_name_list = [
    "unit_test",
    "acceptance_test",
    "integration_test",
    "interface_test",
    "regression_test",
    "sanity_test",
    "smoke_test",
  ]


  React.useEffect(()=>{
    if (test_card_name_list.length > 0){
      console.log('test_card_name_list',test_card_name_list)


      json_fetcher.fetchTestsResultJson()
        .then(r => r.json())
        .then(r_json=>{
          // console.log('r_json',r_json)
          let test_results_list = test_card_name_list.map(x => getResultByTestName(x))
          let number_of_card_per_row = 4

          setShowTestResultList(chunkArray(fillToTheNearestRow(test_results_list,number_of_card_per_row),number_of_card_per_row))
        })


    }
  },[test_card_name_list])




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
            show_test_result_list.map( chunk =>{
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
                            <DoughnutResultCard
                              test_result_to_show={repo_name}
                              result_name={repo_name.name}
                              test_description_unit_test={repo_name.description}
                              />
                          </div>
                        )
                      }
                    })
                  }
                </div>
              )
            })
          }

        </div>
        {/* container */}

      </section>

      <section className={active_style.section}>
        <div className={active_style.container}>
          <h2 className={combineStyles([active_style.title, active_style.is4])} style={{textDecoration:"underline"}}>Time spent</h2>


        </div>

      </section>
    </Layout>
  )
}

export default OverviewPage
