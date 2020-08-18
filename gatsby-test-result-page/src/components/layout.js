/**
 * Layout component that queries for data
 * with Gatsby's useStaticQuery component
 *
 * See: https://www.gatsbyjs.org/docs/use-static-query/
 */

import React from "react"

import ThemeContext from '../contexts/ThemeContext'

function Layout(props){
  const {active_style, rotateStyle} = React.useContext(ThemeContext)

  let {children} = props

  return (
    <>
      <main className={active_style.main}>{children}</main>
    </>
  )
}

export default Layout
