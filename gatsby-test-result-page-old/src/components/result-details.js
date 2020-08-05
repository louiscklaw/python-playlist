import React from 'react'

function ResultDetails(props){
  return(
    <>
      Result details
      <pre>
        {JSON.stringify(props, null, 2)}
      </pre>
    </>
  )
}

export default ResultDetails
