import React from 'react'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {
  faTags
} from '@fortawesome/free-brands-svg-icons'

import ThemeContext from '../contexts/ThemeContext'
import {combineStyles} from '../../utils/common'

function HeadingTags(props){
  const {active_style} =React.useContext(ThemeContext)

  return(
    <>
      <div className={combineStyles([active_style.tag, active_style.isLink])}>
        <FontAwesomeIcon icon={faTags} />
        Link
      </div>
    </>
  )
}

export default HeadingTags