import React from 'react'

import HtmlToReact from  'html-to-react'

import ReactMarkdown from 'react-markdown'
import htmlParser from 'react-markdown/plugins/html-parser'

import {combineStyle} from '../utils/common'

import style from '../scss/style.module.scss'

function custHeaderStyle(level, props){
  switch (level) {
    case 1:
      console.log(props)
      return (<h1 className={combineStyle([style.title, style.is4])}>{props.children}</h1>)
    case 2:
      console.log(props)
      return (<h2 className={combineStyle([style.subtitle, style.is4])}>{props.children}</h2>)
    case 3:
      console.log(props)
      return (<h3 className={combineStyle([style.title, style.is5])}>{props.children}</h3>)
    case 4:
      console.log(props)
      return (<h4 className={combineStyle([style.subtitle, style.is5])}>{props.children}</h4>)
    case 5:
      console.log(props)
      return (<h5 className={combineStyle([style.title, style.is6])}>{props.children}</h5>)
    case 6:
      console.log(props)
      return (<h6 className={combineStyle([style.subtitle, style.is6])}>{props.children}</h6>)

    default:
      return "hello custHeaderStyle"
      break;
  }
}

function TestDescription(props){
  const markdown = props.content

  let processNodeDefinitions = new HtmlToReact.ProcessNodeDefinitions(React);
  let processingInstructions = [
    {
        // Anything else
        shouldProcessNode: function (node) {
          console.log('shouldProcessNode',node)
          console.log('shouldProcessNode','node.parent',node.parent)
          return true;
        },
        processNode: processNodeDefinitions.processDefaultNode
    }
  ];

  const parseHtml = htmlParser({
    isValidNode: node => node.type !== 'script',
    processingInstructions
  })

  return(
    <>
      <ReactMarkdown
        source={markdown}
        escapeHtml={false}
        renderers={{
        heading: props => custHeaderStyle(props.level, props)

        }}
      />
    </>
  )
}

export default TestDescription
