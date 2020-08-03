import unittest
import random

class Test_unit_suite1(unittest.TestCase):
  """
---
Title: basic interface test
Explain: this is basic interface test explain
---
# h1
## h2
### h3

helloworld paragraph

1. hello1
1. hello2
1. hello3
  """

  def test_no_doc_string(self):
    print("no_doc_string")

  def test_helloworld(self):
    """
---
Title: test_helloworld
---
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat.

### basic interface test
    """

    print('hellworld')
