import unittest
import random

class Test_unit_suite1(unittest.TestCase):
  """
  <!-- Test_unit_suite1 docstring -->
  # TestUnitSuite 1

  ## hi can you see me ?
  """

  def test_no_doc_string(self):
    print("no_doc_string")

  def test_helloworld(self):
    """
    # h1
    ## h2
    ### helloworld doc_string
    """
    print('hellworld')
