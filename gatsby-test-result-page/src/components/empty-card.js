import React from 'react'

import {combineStyles} from '../../utils/common'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

import {
  faPaste
} from '@fortawesome/free-solid-svg-icons'

import ThemeContext from '../contexts/ThemeContext'

function EmptyCard(props){
  const {active_style} = React.useContext(ThemeContext)

  return(
    <>
      <div className={active_style.column}>
        {/* empty card */}
      </div>
    </>
  )
}


export default EmptyCard