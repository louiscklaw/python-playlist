import React from "react"

import Footer from './footer'

import ThemeContext from '../contexts/ThemeContext'

function Layout(props){
  const {active_style, rotateStyle} = React.useContext(ThemeContext)

  let {children} = props

  return (
    <>
      <main className={active_style.main}>{children}</main>
      <Footer />
    </>
  )
}

export default Layout
