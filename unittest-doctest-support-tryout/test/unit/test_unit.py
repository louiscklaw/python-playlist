import random
import unittest
import xmlrunner

class TestSequenceFunctions(unittest.TestCase):
  def test_sample(self):
    self.fail('hello fail')
    self.assertTrue(True)

# https://docs.python.org/3.4/library/unittest.html
if __name__ == '__main__':
  with open('test-reports/unit.xml', 'w') as output:
    unittest.main(
      testRunner=xmlrunner.XMLTestRunner(output=output),
      buffer=False,
      catchbreak=False,
      failfast=False,
      verbosity=2
      )

  unitetst.main()