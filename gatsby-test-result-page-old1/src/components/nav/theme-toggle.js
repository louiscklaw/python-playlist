import React from 'react'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSun} from '@fortawesome/free-solid-svg-icons'
import { faMoon} from '@fortawesome/free-solid-svg-icons'

import ThemeContext from '~contexts/themes'

import style from '~scss/style.module.scss'

function ThemeToggle(props){
  let {dark, toggleDark} = React.useContext(ThemeContext)

  return(
    <>
      <a className={style.isPrimary} onClick={(e)=>{ toggleDark(e) }}>
        { dark ? <FontAwesomeIcon icon={faSun} size="2x" />: <FontAwesomeIcon icon={faMoon} size="2x" /> }
      </a>
    </>
  )
}

export default ThemeToggle