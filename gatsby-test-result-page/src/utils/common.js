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

function helloworld() {
  console.log( 'helloworld' )
  return 'helloworld'
}

export {
  helloworld,
  checkTestPassed,
  checkTestError,
  checkTestSkipped
}
