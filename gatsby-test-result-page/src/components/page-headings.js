import React from 'react'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {
  faLink
} from '@fortawesome/free-solid-svg-icons'

import HeadingsTags from './headings-tags'

import ThemeContext from '../contexts/ThemeContext'

const combineStyles = (styles) => styles.join(' ')

function PageHeadings(props){
  const {active_style, rotateStyle} = React.useContext(ThemeContext)

  return(
    <section className={active_style.section} id="content">
  <div className={active_style.container}>
    <div className={combineStyles([active_style.columns, active_style.isDesktop])}>
      {/* column */}
      <div className={combineStyles([active_style.column, active_style.isOneForth])}>
        <div style={{display: 'flex', justifyContent: 'flex-start', flexFlow: 'row'}}>
          <p className={active_style.title}>
            Test progress overview
            <FontAwesomeIcon icon={faLink} />

          </p>
        </div>
        <div className={active_style.content}>
          <div className={active_style.subtitle}>
            showing the overall test status
          </div>
        </div>
      </div>
      {/* column */}
      {/* column */}
      <div className={combineStyles([active_style.column, active_style.isOneForth])}>
        <div style={{display: 'flex', justifyContent: 'flex-start', flexFlow: 'row'}}>
          <div className={active_style.tags} style={{paddingLeft: '1em'}}>
            <HeadingsTags />
            <HeadingsTags />
          </div>
        </div>
      </div>
      {/* column */}
      {/* column */}
      <div className={active_style.column} style={{display: 'flex', alignContent: 'center', textAlign: 'center'}}>
        <div className={active_style.level} style={{width: '100%'}}>
          <div className={combineStyles([active_style.levelItem, active_style.hasTextCentered])}>
            <div>
              <p className={active_style.heading}>Testing passing</p>
              <p className={active_style.title}>111</p>
            </div>
          </div>
          <div className={combineStyles([active_style.levelItem, active_style.hasTextCentered])}>
            <div>
              <p className={active_style.heading}>Test failing</p>
              <p className={active_style.title}>111</p>
            </div>
          </div>
          <div className={combineStyles([active_style.levelItem, active_style.hasTextCentered])}>
            <div>
              <p className={active_style.heading}>Test in-progress</p>
              <p className={active_style.title}>111</p>
            </div>
          </div>
          <div className={combineStyles([active_style.levelItem, active_style.hasTextCentered])}>
            <div>
              <p className={active_style.heading}>Test error</p>
              <p className={active_style.title}>111</p>
            </div>
          </div>
        </div>
      </div>
      {/* column */}
    </div>
  </div>
</section>

  )
}

export default PageHeadings
