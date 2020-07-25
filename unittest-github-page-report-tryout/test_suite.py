from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner

import test_string_methods
# import Example2Test

example_tests = TestLoader().loadTestsFromTestCase(ExampleTests)
suite = TestSuite([example_tests])

# example2_tests = TestLoader().loadTestsFromTestCase(Example2Test)
# suite = TestSuite([example_tests, example2_tests])

kwargs = {
    "output": output_folder_name,
    "report_name": report_name,
    "failfast": True
}
runner = HTMLTestRunner(**kwargs)
runner.run(suite)
