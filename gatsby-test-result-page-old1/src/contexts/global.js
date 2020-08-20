import React from 'react'

import api from '../api'

let default_value = {
  hello: "world",
  python_test_result: {},
  test_result_versions: {}
}

const GlobalContext = React.createContext(default_value)

function GlobalContextProvider(props){
  let [hello, setHello] = React.useState(default_value.hello)

  let [python_test_result, setPythonTestResult] = React.useState(default_value.python_test_result)
  let [test_result_versions, setTestResultVersions] = React.useState(default_value.test_result_versions)

  React.useEffect(()=>{
    console.log('getting python_test_result')

    api.getAllPythonTestResult()
      .then( ( response ) => {
        // setResponseData(response.data)
        console.log( response )
        console.log('typeof response', typeof(response))
        setPythonTestResult(response.data)
      } )
      .catch( ( error ) => {
        console.log( error )
        setPythonTestResult({error:"error during loading the result json"})
      } )

    api.getAppReportVersions()
      .then((response)=>{
        setTestResultVersions(response.data)
      }).catch( ( error ) => {
        console.log( error )

      } )

    },[])

  return(
    <GlobalContext.Provider value={{
      hello, setHello,
      python_test_result, setPythonTestResult,
      test_result_versions, setTestResultVersions
    }}>
      {props.children}
    </GlobalContext.Provider>
  )
}

export {GlobalContextProvider}
export default GlobalContext
