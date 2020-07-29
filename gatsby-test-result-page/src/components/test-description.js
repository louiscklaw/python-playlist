import React from 'react'

import HtmlToReact from  'html-to-react'

import ReactMarkdown from 'react-markdown'
import htmlParser from 'react-markdown/plugins/html-parser'

function MyStyle(level, props){
  return "hello mystyle"
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
        heading: props => MyStyle(props.level, props)

        }}
      />
    </>
  )
}

export default TestDescription
