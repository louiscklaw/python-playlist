/**
 * Implement Gatsby's Node APIs in this file.
 *
 * See: https://www.gatsbyjs.org/docs/node-apis/
 */

// You can delete this file if you're not using it
const fs = require(`fs`)


const getPath = (json_filename) => json_filename.replace(/.json$/,'').replace(/^\.\//,'')

const isTestResultJson = (json_filename) => json_filename.search(/.json$/) > -1

const getTestSuiteName = json_filename => json_filename.match(/(\w+)\.json/)[1]

exports.createPages = ({ actions }) => {
  const { createPage } = actions

  let all_files_in_content_dir = fs.readdirSync('./content').sort()

  let content_urls = all_files_in_content_dir.map(x => `./content/${x}`)

  let result_json_file = content_urls.filter( x => isTestResultJson(x) )

  // for navbar
  let json_files = all_files_in_content_dir.filter( filename => filename.search(/\.json/) > -1)
  let test_types = json_files.map( filename => filename.replace(/\.json/,''))

  console.log('test_types',test_types)

  if (result_json_file.length < 1)  {
    console.log('content_urls',content_urls)
    console.log('result_json_file',result_json_file)
    throw 'cannot find json file in content diretory... '
  }

  result_json_file
    .forEach( json_file_fullpath => {

      if(json_file_fullpath.search(/\.json$/) > -1){
        let json_content = fs.readFileSync(json_file_fullpath,{encoding:'utf-8'})
        let page_path = getPath(json_file_fullpath)

        console.log(`creating page ${page_path}`)

        createPage({
          path: page_path,
          component: require.resolve(`./src/templates/jsonResultTemplate.js`),
          context:{
            testResult: JSON.parse(json_content),
            testSuiteName: getTestSuiteName(json_file_fullpath),
            json_files,
            test_types: test_types
          }
        })

      }
    })

}
