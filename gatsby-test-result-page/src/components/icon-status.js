import {checkTestPassed, checkTestError, checkTestSkipped} from '../utils/common'

import React from 'react'

function IconStatus(props){

  const box_style={
    width: '20px',
    height: '20px'
  }

  const red_box_style={
    ...box_style,
    backgroundColor: '#e74c3c',
  }

  const yellow_box_style={
    ...box_style,
    backgroundColor: '#f1c40f'
  }

  const blue_box_style={
    ...box_style,
    backgroundColor: '#3498db'
  }

  const green_box_style={
    ...box_style,
    backgroundColor: '#2ecc71'
  }

  let selected_box_style =  checkTestPassed(props) ? green_box_style : checkTestError(props) ? red_box_style : checkTestSkipped(props) ? blue_box_style : yellow_box_style

  return(
    <>
      <div className={`box`} style={selected_box_style} />
    </>
  )
}


export default IconStatus