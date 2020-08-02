import unittest
import random

class Test_unit_suite1(unittest.TestCase):
  """
  <!-- Test_unit_suite1 docstring -->
  # TestUnitSuite 1
  """

  def test_no_doc_string():
    print("no_doc_string")

  def test_helloworld():
    """
    # h1
    ## h2
    ### helloworld doc_string
    """
    print('hellworld')
