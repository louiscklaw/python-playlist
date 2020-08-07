import React from 'react'
import {navigate} from 'gatsby'

import Select from 'react-select'

import GlobalContext from '~contexts/global'

import {getResultVersionLink} from '~utils/common'

const options = [
  { value: 'chocolate', label: 'Chocolate' },
  { value: 'strawberry', label: 'Strawberry' },
  { value: 'vanilla', label: 'Vanilla' }
]

function showLoading(){
  return [{ value: 'loading', label: 'loading' }]
}

function handleSelectionChange(selected_item){
  console.log(selected_item)
  navigate(getResultVersionLink())
}

function SelectReportVersions()
{
  let {test_result_versions} = React.useContext(GlobalContext)

  let [select_options, setSelectOptions] = React.useState(showLoading())
  let [select_placeholder, setSelectPlaceholder] = React.useState('loading')

  // console.log('test_result_versions.report_versions',test_result_versions.report_versions)

  React.useEffect(()=>{
    if (test_result_versions.report_versions && test_result_versions.report_versions.length > 0 ){
      setSelectPlaceholder('current version: ')


      setSelectOptions(test_result_versions.report_versions.map(
        (report_version)=> {
          return {
            value: report_version,
            label: report_version
          }
        }))

    }else{
      setSelectPlaceholder('loading')
    }
  },[test_result_versions])

  return(
    <Select
      options={select_options}
      placeholder={select_placeholder}
      onChange={(selected_item) => {handleSelectionChange(selected_item)}}
      />
  )
}

export default SelectReportVersions
