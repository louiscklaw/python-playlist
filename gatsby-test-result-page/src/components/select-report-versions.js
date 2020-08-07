import React from 'react'
import Select from 'react-select'

const options = [
  { value: 'chocolate', label: 'Chocolate' },
  { value: 'strawberry', label: 'Strawberry' },
  { value: 'vanilla', label: 'Vanilla' }
]

const SelectReportVersions = () => (
  <Select
    options={options}
    styles={{backgroundColor: 'red'}}
    />
)

export default SelectReportVersions
