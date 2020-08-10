import axios from 'axios'

const API_ENDPOINT=process.env.API_ENDPOINT

const JSON_ENDPOINT=[API_ENDPOINT,'json'].join('/')

const HELLOWORLD_JSON=[JSON_ENDPOINT,'hello.json'].join('/')
const UNITTEST_RESULT=[JSON_ENDPOINT,'unit.json'].join('/')

const PYTHON_TEST_RESULT=[JSON_ENDPOINT, 'python_test_result.json'].join('/')
const ALL_REPORT_VERSIONS=[JSON_ENDPOINT,'report_version_catalogue.json'].join('/')

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

function getAppReportVersions(){
  return getData(ALL_REPORT_VERSIONS)
}

function getAllPythonTestResult(){
  return getData(PYTHON_TEST_RESULT)
}

function getUnittestResult(){
  return getData(UNITTEST_RESULT)
}

function getHelloworld(){
  return getData(HELLOWORLD_JSON)
}

export default {
  getHelloworld, getUnittestResult, getAllPythonTestResult, getAppReportVersions
}