import React from 'react'
import {Link} from 'gatsby'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

import { faGithub } from '@fortawesome/free-brands-svg-icons'
import { faSun} from '@fortawesome/free-solid-svg-icons'
import { faMoon} from '@fortawesome/free-solid-svg-icons'


import SelectReportVersions from '~components/select-report-versions'

import style from '~scss/style.module.scss'

import GlobalContext from '~contexts/global'

const combineStyle = (styles) => styles.join(' ')

const findInArray = (ele, items) => items.indexOf(ele) > -1

function TopNavList({test_types}){
  const items_order = ['smoke_test','unit_test','integration_test']

  let items_in_report = test_types

  return(
    <>
    {
      // list the items with order configured
      items_order.map( nav_item => {
        if (findInArray(nav_item, items_in_report)) {
          items_in_report = items_in_report.filter( x => x != nav_item)
          return(
            <Link to={`/content/${nav_item}`} className={style.navbarItem}>
              {nav_item}
            </Link>
          )
        }
      })
    }

    {
      items_in_report.map( nav_item => {
        return(
          <Link to={`/content/${nav_item}`} className={style.navbarItem}>
            {nav_item}
          </Link>
        )
      })
    }
    </>
  )
}


function Navbar(props){
  const { python_test_result } = React.useContext(GlobalContext)

  let [test_types, setTestTypes] = React.useState([])

  let {active_test_type, current_report_version} = props

  // console.log('active_test_type', active_test_type)
  // console.log('current_report_version',current_report_version)

  React.useEffect(()=>{
    console.log('python_test_result.keys',python_test_result)
    setTestTypes(Object.keys(python_test_result))
  },[python_test_result])

  return(
    <>
      <nav className={style.navbar} role="navigation" aria-label="main navigation">
        <div className={style.navbarBrand}>
          <a className={style.navbarItem} href="https://louiscklaw.github.io">

            <div style={{ fontFamily: 'Indie Flower', fontSize:'x-large' }}>
              Test report
            </div>

          </a>

          {/* hamburger button */}
          <a role="button" className={[style.navbarBurger, style.burger]} aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
          {/* hamburger button */}

        </div>
        {/* navbarBrand */}


        {/* navbarBasicExample */}
        <div id="navbarBasicExample" className={style.navbarMenu}>
          <div className={style.navbarStart}>
            <Link to="/statistics" className={style.navbarItem}> Statistics </Link>

            <TopNavList test_types={test_types} />

            {/* navbar->more */}
            <div className={combineStyle([style.navbarItem, style.hasDropdown, style.isHoverable])}>
              <a className={style.navbarLink}>
                More
              </a>

              <div className={style.navbarDropdown}>
                <Link to='/about' className={style.navbarItem}>About</Link>
                <a className={style.navbarItem}> Documentation </a>
                <a className={style.navbarItem}> Report an issue </a>
              </div>
            </div>
            {/* navbar->more */}


          </div>

          {/* navbarEnd */}
          <div className={style.navbarEnd}>

            {/* AUT version select */}
            <div className={style.navbarItem}>
              <div style={{width:"200px"}}>
                <SelectReportVersions
                  test_type={active_test_type}
                  current_report_version={current_report_version}
                  />
              </div>
            </div>
            {/* AUT version select */}

            {/* github source link */}
            <div className={style.navbarItem}>
              <a className={style.isPrimary}>
                <FontAwesomeIcon icon={faSun} size="2x" />
                <FontAwesomeIcon icon={faMoon} size="2x" />
                <FontAwesomeIcon icon={faGithub} size="2x" />
              </a>
            </div>
            {/* github source link */}

          </div>
          {/* navbarEnd */}

        </div>
        {/* navbarBasicExample */}


      </nav>
    </>
  )
}

export default Navbar