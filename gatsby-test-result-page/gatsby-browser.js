/**
 * Implement Gatsby's Browser APIs in this file.
 *
 * See: https://www.gatsbyjs.org/docs/browser-apis/
 */

// You can delete this file if you're not using it
import React from "react"

import { GlobalContextProvider } from "~contexts/global"


export const wrapRootElement = ({ element }) => (
  <GlobalContextProvider>
    {element}
  </GlobalContextProvider>
)
