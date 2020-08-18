import React from "react"

import { ThemeContextProvider } from "./src/contexts/ThemeContext"

export const wrapRootElement = ({ element }) => (
  <ThemeContextProvider>
    {element}
  </ThemeContextProvider>
)
