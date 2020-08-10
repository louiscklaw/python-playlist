import React from 'react'
import {Link} from 'gatsby'

import style from '../../scss/style.module.scss'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faGithub, faBug } from '@fortawesome/free-brands-svg-icons'

const combineStyle = (styles) => styles.join(' ')

function Navbar(props){
  return(
    <nav className={style.navbar} role="navigation" aria-label="main navigation">
      <div className={style.navbarBrand}>

        <a className={style.navbarItem} href="dashboard.html">
          <FontAwesomeIcon icon={faGithub} size="2x" />
          Simple test report
        </a>

        <a role="button" className={[style.navbarBurger, style.burger]} aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" className={style.navbarMenu}>
        <div className={style.navbarStart}>

          <Link to="/overview" className={style.navbarItem} >Overview</Link>
          <Link to="/smoke_test" className={style.navbarItem}>smoke_test</Link>
          <Link to="/unit_test" className={style.navbarItem}>unit_test</Link>
          <Link to="/integration_test" className={style.navbarItem}>integration_test</Link>
          <Link to="/acceptance_test" className={style.navbarItem}>acceptance_test</Link>
          <Link to="/interface_test" className={style.navbarItem}>interface_test</Link>
          <Link to="/regression_test" className={style.navbarItem}>regression_test</Link>
          <Link to="/sanity_test" className={style.navbarItem}>sanity_test</Link>


          <a className={style.navbarItem}> Documentation </a>

          <div className={combineStyle([style.navbarItem, style.hasDropdown, style.isHoverable])}>
            <a className={style.navbarLink}>
              More
            </a>

            <div className={style.navbarDropdown}>

              <a className={style.navbarItem}> About </a>

            </div>
          </div>
        </div>

        <div className={style.navbarEnd}>
          <div className={style.navbarItem}>
            <div className={style.buttons}>
              <a className={combineStyle([style.button, style.isWhite])}>
                <FontAwesomeIcon icon={faGithub} size="2x" />
                <p style={{margin: '0 0.3rem'}}>Github source</p>
              </a>
            </div>
          </div>
        </div>

      </div>
    </nav>
  )
}

export default Navbar
