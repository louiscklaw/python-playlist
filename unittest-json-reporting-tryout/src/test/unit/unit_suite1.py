import unittest
import random

class Test_unit_suite1(unittest.TestCase):
  """
---
Title: basic interface test(Test_unit_suite1)
Explain: this is basic interface test explain
---
UNIT TESTING is a level of software testing where individual units/ components of a software are tested. The purpose is to validate that each unit of the software performs as designed. A unit is the smallest testable part of any software. It usually has one or a few inputs and usually a single output.

可以降低日後的維護成本；對於會TDD (Test-Driven Development)的工程師來說，甚至是加快開發速度。 程式碼品質. 程式碼的品質最主要的
  """

  def test_no_doc_string(self):
    print("no_doc_string")

  def test_helloworld(self):
    """
---
Title: test_helloworld
---
# h1
## h2
### h3

helloworld paragraph

1. hello1
1. hello2
1. hello3
    """

    print('hellworld')
