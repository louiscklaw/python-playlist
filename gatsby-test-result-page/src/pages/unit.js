import React from 'react'

import Navbar from '~components/nav'

import PreJson from '~components/pre-json'
import PreUnittest from '~components/pre-unittest'

import GlobalContext from '~contexts/global'

function UnitTestResultPage(props){
  let global_context = React.useContext(GlobalContext)

  return(
    <>
      {global_context.hello}
      unittest result page
      <Navbar />
      update 123321

      {/* <PreUnittest /> */}
      {JSON.stringify(global_context.python_test_result, null, 2)}
    </>
  )
}

export default UnitTestResultPage
