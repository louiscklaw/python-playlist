import axios from 'axios'

const API_ENDPOINT="https://raw.githubusercontent.com/louiscklaw/python-playlist/gh-pages"
const HELLOWORLD_JSON=API_ENDPOINT+'/'+'json/hello.json'


export default {
  getData: () =>
  axios({
      'method':'GET',
      'url': HELLOWORLD_JSON,
      'headers': {
          'content-type':'application/octet-stream'
      },
      // 'params': {
      //     'search':'parameter',
      // },
  })
}