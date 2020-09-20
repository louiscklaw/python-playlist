import React from "react"

import { ThemeContextProvider } from "./src/contexts/ThemeContext"
import { ResultContextProvider } from "./src/contexts/ResultContext"
import { ConfigContextProvider } from "./src/contexts/ConfigContext"

export const wrapRootElement = ({ element }) => (
  <ThemeContextProvider>
    <ConfigContextProvider>
      <ResultContextProvider>
        {element}
      </ResultContextProvider>
    </ConfigContextProvider>
  </ThemeContextProvider>
)
