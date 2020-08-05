import axios from 'axios'

const API_ENDPOINT="https://raw.githubusercontent.com/louiscklaw/python-playlist/gh-pages"

const JSON_ENDPOINT=[API_ENDPOINT,'json'].join('/')

const HELLOWORLD_JSON=[JSON_ENDPOINT,'hello.json'].join('/')
const UNITTEST_RESULT=[JSON_ENDPOINT,'unit.json'].join('/')


function getData(resource_url){
  return   axios({
    'method':'GET',
    'url': resource_url,
    'headers': {
        'content-type':'application/octet-stream'
    },
    // 'params': {
    //     'search':'parameter',
    // },
})
}

export default {
  getHelloworld: () => getData(HELLOWORLD_JSON),

  getUnittestResult: () =>  getData(UNITTEST_RESULT)

}