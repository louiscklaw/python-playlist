import React from 'react'

let default_value = {
  hello: "world",
}

const UiContext = React.createContext(default_value)

function UiContextProvider(props){
  let [hello, setHello] = React.useState(default_value.hello)

  React.useEffect(()=>{

  },[])

  return(
    <UiContext.Provider value={{
      hello, setHello
    }}>
      {props.children}
    </UiContext.Provider>
  )
}

export {UiContextProvider}
export default UiContext
