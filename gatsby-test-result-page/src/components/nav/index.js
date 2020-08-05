import React from 'react'
import {Link} from 'gatsby'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faGithub } from '@fortawesome/free-brands-svg-icons'

import style from '~scss/style.module.scss'

import GlobalContext from '~contexts/global'

const combineStyle = (styles) => styles.join(' ')


function Navbar(props){
  const { python_test_result } = React.useContext(GlobalContext)

  let [test_type, setTestType] = React.useState([])

  React.useEffect(()=>{

    setTestType(Object.keys(python_test_result))

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

            {
              test_type.map( nav_item => {
                return(
                  <Link to={`/content/${nav_item}`} className={style.navbarItem}> {nav_item} </Link>
                )
              })
            }


            {/* navbar->more */}
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
            {/* navbar->more */}


          </div>

          {/* navbarEnd */}
          <div className={style.navbarEnd}>
            <div className={style.navbarItem}>
              <div className={style.buttons}>
                <a className={combineStyle([style.button, style.isPrimary])} href="https://www.github.com/louiscklaw/python-playlist">
                  <FontAwesomeIcon icon={faGithub} size="2x" />
                </a>
              </div>
            </div>
          </div>
          {/* navbarEnd */}

        </div>
        {/* navbarBasicExample */}


      </nav>
    </>
  )
}

export default Navbar