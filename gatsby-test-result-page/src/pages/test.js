import React from 'react'
import {helloUtil, fillToTheNearestRow, chunkArray} from '../../utils/common'

function printError(msg, obj){
  console.log(msg, obj)

}

function compareObject(oA, oB){
  return JSON.stringify(oA) == JSON.stringify(oB)
}

function TestBody(){

    // helloworld test
    // console.assert(helloUtil()=='helloUtil', 'hello failure')

    // fillToTheNearestRow
    let test_filltothenearestrow = fillToTheNearestRow([1,2,3,4,5],4)
    console.assert(compareObject(test_filltothenearestrow,[1,2,3,4,5,null,null,null]), 'fillToTheNearestRow fail')
    // console.log('fillToTheNearestRow',fillToTheNearestRow([1,2,3,4,5],4))

    // chunkArray
    let test_chunk_array = chunkArray([1,2,3,4,5,6],4)
    console.assert(compareObject(test_chunk_array, [[1,2,3,4],[5,6]]), 'chunkArray failure')

    let test_result = chunkArray(fillToTheNearestRow([1,2,3,4,5,6],4), 4)
    console.assert(compareObject(test_result, [[1,2,3,4],[5,6,null,null]]))


}


function TestPage(props){
  let [error_display, setErrorDisplay] = React.useState('hello error display')

  React.useEffect(()=>{
    TestBody()
  },[])

  return(
    <>
      <div>
        test page
      </div>

      <div style={{color:'red'}}>
        { error_display }
      </div>

    </>
  )
}

export default TestPage