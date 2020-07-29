import React from 'react'
import {Link} from 'gatsby'

import style from '../../scss/style.module.scss'

const combineStyle = (styles) => styles.join(' ')

function Navbar(props){
  return(
    <nav className={style.navbar} role="navigation" aria-label="main navigation">
      <div className={style.navbarBrand}>
        <a className={style.navbarItem} href="https://bulma.io">
          <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28" />
        </a>

        <a role="button" className={[style.navbarBurger, style.burger]} aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" className={style.navbarMenu}>
        <div className={style.navbarStart}>

        <Link to="/content/unit" className={style.navbarItem}> Unit </Link>
        <Link to="/content/integration" className={style.navbarItem}> Integration </Link>
        <Link to="/content/system" className={style.navbarItem}> System </Link>
        <Link to="/content/sanity" className={style.navbarItem}> Sanity </Link>
        <Link to="/content/smoke" className={style.navbarItem}> Smoke </Link>
        <Link to="/content/interface" className={style.navbarItem}> Interface </Link>
        <Link to="/content/regression" className={style.navbarItem}> Regression </Link>
        <Link to="/content/acceptance" className={style.navbarItem}> Acceptance </Link>

        <Link to="/statistics" className={style.navbarItem}> Statistics </Link>

          <div className={combineStyle([style.navbarItem, style.hasDropdown, style.isHoverable])}>
            <a className={style.navbarLink}>
              More
            </a>

            <div className={style.navbarDropdown}>
              <a className={style.navbarItem}> About </a>
              <a className={style.navbarItem}> Documentation </a>
              <a className={style.navbarItem}> Report an issue </a>
            </div>

          </div>
        </div>

        <div className={style.navbarEnd}>
          <div className={style.navbarItem}>
            <div className={style.buttons}>
              <a className={combineStyle([style.button, style.isPrimary])}>
                source code
              </a>
            </div>
          </div>
        </div>
      </div>
    </nav>
  )
}

export default Navbar
