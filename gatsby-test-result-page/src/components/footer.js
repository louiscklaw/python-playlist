import React from 'react'
import {Link} from 'gatsby'

import style from '../scss/style.module.scss'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faGithub, faBug } from '@fortawesome/free-brands-svg-icons'

import {combineStyle} from '../../utils/common'

function Footer(props){
  return(


  <footer className={style.footer}>
    <div className={combineStyle([style.content, style.hasTextCentered])}>
      <div className={style.container}>

        <p> Simple test report for xxxxx </p>

        <a className={combineStyle([style.button, style.isSmall, style.isWhite])} href="//www.github.com/louiscklaw" target="_blank">
          <FontAwesomeIcon icon={faGithub} size="2x" />
          <span style={{paddingLeft: '0.5rem'}}>www.github.com/louiscklaw</span>
        </a>

      </div>
    </div>
  </footer>

  )
}


export default Footer