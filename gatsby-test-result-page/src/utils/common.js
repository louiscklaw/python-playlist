const checkSkippedKeyExist = ( test_detail_json ) => Object.keys( test_detail_json ).indexOf( "skipped" ) > -1

const checkErrorKeyExist = ( test_detail_json ) => Object.keys( test_detail_json ).indexOf( "error" ) > -1

const checkTestPassed = ( test_detail_json ) => {
  return !(checkErrorKeyExist( test_detail_json ) || checkSkippedKeyExist( test_detail_json ))
}

const checkTestError = ( test_detail_json ) => {
  return checkErrorKeyExist( test_detail_json )
}

const checkTestSkipped = ( test_detail_json ) => {
  return checkSkippedKeyExist( test_detail_json )
}

const combineStyle = (styles) => styles.join(' ')

function helloworld() {
  console.log( 'helloworld' )
  return 'helloworld'
}

const getReportVersionLink = (test_type, report_ver) => `${report_ver}/${test_type}`

export {
  helloworld,
  checkTestPassed,
  checkTestError,
  checkTestSkipped,
  combineStyle,

  getReportVersionLink
}
