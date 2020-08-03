https://github.com/xmlrunner/unittest-xml-reporting


### markdowns
- markdown tried best to follow github markdown spec.
https://github.com/rexxars/react-markdown

- meta of test type is defined in `src/reports_meta/{test_type}/desc.md`

### to generate testcases

`scripts/gen_tests/run.sh`

paths:

file:
  test/unit/unit_suite1

class:
  (test_types).(testsuite_filenames).(testsuite_classnames).(testcase_names)
  (test_type).(testsuite_filename).(testsuite_classname).(testcase_name)

  unit.unit_suite1.Test_unit_suite1.test_helloworld

json:
  reports/testsuite/testcase/unit_suite1.Test_unit_suite1/test_helloworld
