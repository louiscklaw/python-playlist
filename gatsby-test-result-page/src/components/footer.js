import React from 'react'
import {Link} from 'gatsby'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
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

import {
  faGithubSquare,
  faFacebookSquare,
  faLinkedin,
  faTwitter,
} from '@fortawesome/free-brands-svg-icons'

import ThemeContext from '../contexts/ThemeContext'

import {combineStyles} from '../../utils/common'

function Footer(props){
  const {active_style} = React.useContext(ThemeContext)

  return(
    <>
      {/* footer */}
      <footer className={active_style.footer}>
        <div className={combineStyles([active_style.content, active_style.hasTextCentered])}>
          <div className={active_style.container}>
            <p> Simple test report for xxxxx </p>
            <a className={combineStyles([active_style.button, active_style.isPrimary, active_style.isInverted, active_style.isSmall])} href="//www.github.com/louiscklaw" target="_blank">
              <FontAwesomeIcon icon={faGithubSquare} style={{fontSize:'1.33em'}}/>
              <span style={{paddingLeft: '0.5rem'}}>www.github.com/louiscklaw</span>
            </a>
            <a className={combineStyles([active_style.button, active_style.isPrimary, active_style.isInverted, active_style.isSmall])} href="//www.facebook.com/louiscklaw" target="_blank">
              <FontAwesomeIcon icon={faFacebookSquare} style={{fontSize:'1.33em'}}/>
              <span style={{paddingLeft: '0.5rem'}}>www.facebook.com/louiscklaw</span>
            </a>
            <a className={combineStyles([active_style.button, active_style.isPrimary, active_style.isInverted, active_style.isSmall])} href="//www.linkedin.com/in/louiscklaw" target="_blank">
              <FontAwesomeIcon icon={faLinkedin} style={{fontSize:'1.33em'}}/>
              <span style={{paddingLeft: '0.5rem'}}>www.linkedin.com/in/louiscklaw</span>
            </a>
          </div>
        </div>
        <div className={combineStyles([active_style.content, active_style.hasTextCentered])}>
          <div className={active_style.container}>
            <p> 💖 coded by louiscklaw. 2020 </p>
          </div>
        </div>
      </footer>
      {/* footer */}

    </>
  )
}


export default Footer