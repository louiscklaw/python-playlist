import unittest
import random

class Test_integration_suite1(unittest.TestCase):
  """
  # helloworld h1

  ## This is an h2 tag

  ### This is an h3 tag

  #### This is an h4 tag

  ##### This is an h5 tag

  ###### This is an h6 tag


  I think you should use an
  `<addr>` element here instead.

  First Header | Second Header
  ------------ | -------------
  Content from cell 1 | Content from cell 2
  Content in the first column | Content in the second column

  - white box test
  - test by functions
  """

  def test_sample_0(self):
    """ passed template """
    self.assertTrue(True)

  def test_sample_1(self):
    """ passed template """
    self.assertTrue(True)
