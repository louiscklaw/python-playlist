import React from 'react'

function ResultContent(props){
  return(
    <>
      result content
      {
        JSON.stringify(props.test_type, null, 2)
      }
    </>
  )
}


export default ResultContent