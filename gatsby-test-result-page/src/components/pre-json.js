import React from 'react'

import api from '../api'

function PreJson(props){
  let [ responseData, setResponseData ] = React.useState( 'loading' )

  React.useEffect( () => {
    fetchData()
  }, [] )

  // fetches data
  const fetchData = ( ) => {
    // e.preventDefault()

    api.getData()
      .then( ( response ) => {
        // setResponseData(response.data)
        console.log( response )
        setResponseData(response.data)
      } )
      .catch( ( error ) => {
        console.log( error )
        setResponseData('error during loading the result json')
      } )
  }


  return(
    <>
      <pre>
        {JSON.stringify(responseData, null, 2)}
      </pre>
    </>
  )
}

export default PreJson