# regenerate test result

`$ ./regen_test_result.sh`

### To run
```
$ cd src
$ ./run.sh
```


### mapping table

- unittest: python-playlist/unittest-json-reporting-tryout
- report page: python-playlist/gatsby-test-result-page

| unittest      | report page |
| ------------- | ------------- |
| test_unit.json  | 即係 page 啦 (http://localhost:8000/content/unit) |
| testsuites/reports [1,2,3...]  | test-suites.js (幾張咭走埋一齊)?|
| testsuite  |  card.js (好多粒 status 走出黎) |
| testcase[1,2,3...] | icon-status.js / result-details.js |

### dev:
to regenerate the test result
`regen_test_result.sh`

## Background information for tests:

### Functional Testing types include:

- Unit
- Integration
- System
- Sanity
- Smoke
- Interface
- Regression
- Beta/Acceptance

### Non-functional Testing types include:

- Performance Testing
- Load Testing
- Stress Testing
- Volume Testing
- Security Testing
- Compatibility Testing
- Install Testing
- Recovery Testing
- Reliability Testing
- Usability Testing
- Compliance Testing
- Localization Testing