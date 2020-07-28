/**
 * Implement Gatsby's Node APIs in this file.
 *
 * See: https://www.gatsbyjs.org/docs/node-apis/
 */

// You can delete this file if you're not using it
const fs = require(`fs`)
const yaml = require(`js-yaml`)

const path = require(`path`)

const getPath = (json_filename) => json_filename.replace(/.json$/,'').replace(/^\.\//,'')

const isTestResultJson = (json_filename) => json_filename.search(/.json$/) > -1

exports.createPages = ({ actions }) => {
  const { createPage } = actions
  let files_in_content = fs.readdirSync('./content').map(x => `./content/${x}`)

  console.log(files_in_content)

  files_in_content
    .filter( x => isTestResultJson(x) )
    .forEach( json_file_fullpath => {
      if(json_file_fullpath.search(/\.json$/) > -1){
        let json_content = fs.readFileSync(json_file_fullpath,{encoding:'utf-8'})
        let page_path = getPath(json_file_fullpath)

        console.log(`creating page ${page_path}`)

        createPage({
          path: page_path,
          component: require.resolve(`./src/templates/jsonResultTemplate.js`),
          context:{
            testResult: JSON.parse(json_content)
          }
        })

      }else{
        // console.log(`skipping generate page as not json file ${json_file_fullpath}`)
      }
    })

}
