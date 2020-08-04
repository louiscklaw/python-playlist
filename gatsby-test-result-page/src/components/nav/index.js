import React from 'react'
import {Link} from 'gatsby'

import style from '../../scss/style.module.scss'

const combineStyle = (styles) => styles.join(' ')

function Navbar(props){
  return(
    <nav className={style.navbar} role="navigation" aria-label="main navigation">
      <div className={style.navbarBrand}>
        <a className={style.navbarItem} href="https://louiscklaw.github.io">

          <div style={{ fontFamily: 'Indie Flower', fontSize:'x-large' }}>
            Test report
          </div>

        </a>

        <a role="button" className={[style.navbarBurger, style.burger]} aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" className={style.navbarMenu}>
        <div className={style.navbarStart}>

        <Link to="/statistics" className={style.navbarItem}> Statistics </Link>

        {
          props.nav_items.map( nav_item => {
            return(
              <Link to={`/content/${nav_item}`} className={style.navbarItem}> {nav_item} </Link>
            )
          })
        }

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
