import React from 'react'
import { navigate } from 'gatsby'

import Select from 'react-select'

import GlobalContext from '~contexts/global'

import {getResultVersionLink} from '~utils/common'

function showLoading(){
  return [{ value: 'loading', label: 'loading' }]
}

function SelectReportVersions(props)
{
  let {test_result_versions} = React.useContext(GlobalContext)

  let [select_options, setSelectOptions] = React.useState(null)
  let [select_placeholder, setSelectPlaceholder] = React.useState('loading ... ')

  let [current_report_version, setCurrentReportVersion] = React.useState(props.current_report_version)
  let [select_selected, setSelectSelected] = React.useState(null)

  const getValues = (value, o) => Object.values(o)
  const valueExistInObj = (value, o) => getValues(o).indexOf(value) > -1
  const lookupByValue = (value, o) => getValues(o).indexOf(value)

  const handleSelectChange = (selected_item) => {
    let selected_value = selected_item.value
    console.log('select-report-versions.props',props)
    let {test_type} = props
    navigate(`/content/${test_type}/${selected_value}`)
    setSelectSelected(selected_item)
  }

  React.useEffect(()=>{
    if (test_result_versions.report_versions && test_result_versions.report_versions.length > 0 ){
      let all_select_options = test_result_versions.report_versions.map(
        ( report_version ) => {
          return {
            value: report_version,
            label: report_version
          }
        } )
        setSelectOptions( all_select_options )

        if (typeof(current_report_version) == 'undefined'){
          // url contain no version information, do nothing
        }else{
          console.log('current_report_version', current_report_version)
          let idx = Object.values(all_select_options).map((x) => x.value).indexOf(current_report_version)
          setSelectSelected(all_select_options[idx])
        }

      }
  },[test_result_versions])



  return(
    <Select
      options={select_options}
      placeholder={'trunk ... '}
      onChange={(selected_item) => {handleSelectChange(selected_item)}}

      value={select_selected}

      />
  )
}

export default SelectReportVersions
