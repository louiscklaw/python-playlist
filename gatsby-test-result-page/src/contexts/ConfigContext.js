import React from 'react'

const chart_colors = [
  '#2ecc71',
  '#e74c3c',
  '#f1c40f',
  '#95a5a6'
]

const default_value ={
  hello:'world'
}
const ConfigContext = React.createContext(default_value)

const default_chart_config ={
  type: "doughnut",
  options: {
    aspectRatio: 1,
    responsive: true,
    legend: {
      position: "right",
    },
    animation: {
      animateScale: true,
      animateRotate: true
    }
  }
}

function ConfigContextProvider(props){
  let {children} = props
  const [hello, setHello] = React.useState(null)
  const [chart_config, setChartConfig]= React.useState(default_chart_config)


  return(
    <>
      <ConfigContext.Provider value={{
        hello, setHello,
        chart_config,
        chart_colors
      }}>
        {children}
      </ConfigContext.Provider>
    </>
  )
}

export default ConfigContext

export {ConfigContextProvider}
