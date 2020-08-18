import React from 'react'
import {Link} from 'gatsby'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {
  faGithub,
} from '@fortawesome/free-brands-svg-icons'

import {
  faPalette,
  faQuestionCircle,
  faRoad,
  faCodeBranch,
  faClock,
  faBook,
  faBug,
  faLanguage
} from '@fortawesome/free-solid-svg-icons'

import ThemeContext from '../../contexts/ThemeContext'

const combineStyles = (styles) => styles.join(' ')

function NavIndex(props){
  const {active_style, rotateStyle} = React.useContext(ThemeContext)

  return(
    <nav className={active_style.navbar} role="navigation" aria-label="main navigation">
  <div className={active_style.navbarBrand}>
    <a className={active_style.navbarItem} href="overview.html">
      Simple test report
    </a>
    <a role="button" className={combineStyles([active_style.navbarBurger, active_style.burger])} aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
      <span aria-hidden="true" />
      <span aria-hidden="true" />
      <span aria-hidden="true" />
    </a>
  </div>
  <div id="navbarBasicExample" className={active_style.navbarMenu}>
    <div className={active_style.navbarStart}>
      <a className={combineStyles([active_style.navbarItem, active_style.isActive])} href="dashboard.html">
        Overview
      </a>
      <a className={active_style.navbarItem} href="test-report-content.html">
        smoke_test </a>
      <a className={active_style.navbarItem}>
        unit_test
      </a>
      <a className={active_style.navbarItem}>
        integration_test
      </a>
      <a className={active_style.navbarItem}>
        acceptance_test
      </a>
      <a className={active_style.navbarItem}>
        interface_test
      </a>
      <a className={active_style.navbarItem}>
        regression_test
      </a>
      <a className={active_style.navbarItem}>
        sanity_test
      </a>
      <div className={combineStyles([active_style.navbarItem, active_style.hasDropdown, active_style.isHoverable])}>
        <a className={active_style.navbarLink}>
          More
        </a>
        <div className={active_style.navbarDropdown}>
          {/* navbar-item */}
          <a href="time_analysis.html" className={active_style.navbarItem}>
            <div className={combineStyles([active_style.level, active_style.isMobile])}>
              <div className={active_style.levelLeft}>
                <div className={active_style.levelItem}>
                  <p>
                    <FontAwesomeIcon icon={faBook} />
                    <strong>Documentation</strong>
                    <br />
                    <small>time used for the tests</small>
                  </p>
                </div>
              </div>
            </div>
          </a>
          {/* navbar-item */}
          {/* navbar-item */}
          <a href="time_analysis.html" className={active_style.navbarItem}>
            <div className={combineStyles([active_style.level, active_style.isMobile])}>
              <div className={active_style.levelLeft}>
                <div className={active_style.levelItem}>
                  <p>
                    <FontAwesomeIcon icon={faClock} />
                    <strong>time analysis</strong>
                    <br />
                    <small>time used for the tests</small>
                  </p>
                </div>
              </div>
            </div>
          </a>
          {/* navbar-item */}
          {/* navbar-item */}
          <a href="chartjs_test.html" className={active_style.navbarItem}>
            <div className={combineStyles([active_style.level, active_style.isMobile])}>
              <div className={active_style.levelLeft}>
                <div className={active_style.levelItem}>
                  <p>
                    <FontAwesomeIcon icon={faCodeBranch} />
                    <strong>chartjs test</strong>
                    <br />
                    <small>back stage to test chartjs api</small>
                  </p>
                </div>
              </div>
            </div>
          </a>
          {/* navbar-item */}
          {/* navbar-item */}
          <a href="roadmap.html" className={active_style.navbarItem}>
            <div className={combineStyles([active_style.level, active_style.isMobile])}>
              <div className={active_style.levelLeft}>
                <div className={active_style.levelItem}>
                  <p>
                    <FontAwesomeIcon icon={faRoad} />
                    <strong>Roadmap</strong>
                    <br />
                    <small>simple plan of this test report</small>
                  </p>
                </div>
              </div>
            </div>
          </a>
          {/* navbar-item */}
          {/* navbar-item */}
          <a href="about.html" className={active_style.navbarItem}>
            <div className={combineStyles([active_style.level, active_style.isMobile])}>
              <div className={active_style.levelLeft}>
                <div className={active_style.levelItem}>
                  <p>
                    <FontAwesomeIcon icon={faQuestionCircle} />
                    <strong>About this page</strong>
                    <br />
                    <small>Side projects to enhance Bulma</small>
                  </p>
                </div>
              </div>
            </div>
          </a>
          {/* navbar-item */}
        </div>
      </div>
      <div className={active_style.navbarItem}>
        <div className={combineStyles([active_style.select, active_style.isSmall])} style={{color: '#34495e'}}>
          <select>
            <option>Select version</option>
            <option>options version 1</option>
            <option>options version 2</option>
            <option>options version 3</option>
            <option>options version 4</option>
            <option>options version 5</option>
            <option>options version 6</option>
            <option>options version 7</option>
            <option>options version 8</option>
          </select>
        </div>
      </div>
    </div>
    <div className={active_style.navbarEnd}>
      <div className={active_style.navbarItem}>
        <div className={active_style.buttons}>
          {/* navbar-item */}
          <a href="about.html" className={active_style.navbarItem}>
            <div className={combineStyles([active_style.level, active_style.isMobile])}>
              <div className={active_style.levelLeft}>
                <div className={active_style.levelItem}>
                  <p>
                    <FontAwesomeIcon icon={faLanguage} />
                  </p>
                </div>
              </div>
            </div>
          </a>
          {/* navbar-item */}
          {/* navbar-item */}
          <a href="about.html" className={active_style.navbarItem}>
            <div className={combineStyles([active_style.level, active_style.isMobile])}>
              <div className={active_style.levelLeft}>
                <div className={active_style.levelItem}>
                  <p>
                    <FontAwesomeIcon icon={faPalette} />
                  </p>
                </div>
              </div>
            </div>
          </a>
          {/* navbar-item */}
          {/* navbar-item */}
          <a href="about.html" className={active_style.navbarItem}>
            <div className={combineStyles([active_style.level, active_style.isMobile])}>
              <div className={active_style.levelLeft}>
                <div className={active_style.levelItem}>
                  <p>
                    <FontAwesomeIcon icon={faBug} />
                  </p>
                </div>
              </div>
            </div>
          </a>
          {/* navbar-item */}
          {/* navbar-item */}
          <a href="about.html" className={active_style.navbarItem}>
            <div className={combineStyles([active_style.level, active_style.isMobile])}>
              <div className={active_style.levelLeft}>
                <div className={active_style.levelItem}>
                  <p>
                    <FontAwesomeIcon icon={faGithub} />
                  </p>
                </div>
              </div>
            </div>
          </a>
          {/* navbar-item */}
        </div>
      </div>
    </div>
  </div>
</nav>

  )
}

export default NavIndex
