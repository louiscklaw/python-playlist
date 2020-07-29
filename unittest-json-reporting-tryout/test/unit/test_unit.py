import random
import unittest
import xmlrunner

class TestSuite1(unittest.TestCase):
  """suite description"""

  def setUp(self):
    self.seq = list(range(10))

  @unittest.skip("demonstrating skipping")
  def test_skipped(self):
    self.fail("shouldn't happen")

  def test_shuffle(self):
    # make sure the shuffled sequence does not lose any elements
    random.shuffle(self.seq)
    self.seq.sort()
    self.assertEqual(self.seq, list(range(10)))

    # should raise an exception for an immutable sequence
    self.assertRaises(TypeError, random.shuffle, (1,2,3))



class TestSuite2(unittest.TestCase):
  """suite2 description"""

  def setUp(self):
    self.seq = list(range(10))

  @unittest.skip("demonstrating skipping")
  def test_skipped(self):
    self.fail("shouldn't happen")

  def test_shuffle(self):
    # make sure the shuffled sequence does not lose any elements
    random.shuffle(self.seq)
    self.seq.sort()
    self.assertEqual(self.seq, list(range(10)))

    # should raise an exception for an immutable sequence
    self.assertRaises(TypeError, random.shuffle, (1,2,3))

  def test_choice(self):
    element = random.choice(self.seq)
    self.assertTrue(element in self.seq)

  def test_sample(self):
    with self.assertRaises(ValueError):
      random.sample(self.seq, 20)
    for element in random.sample(self.seq, 5):
      self.assertTrue(element in self.seq)

class TestSuite3(unittest.TestCase):
  """suite2 description"""

  def setUp(self):
    self.seq = list(range(10))

  @unittest.skip("demonstrating skipping")
  def test_skipped(self):
    self.fail("shouldn't happen")

  def test_shuffle(self):
    # make sure the shuffled sequence does not lose any elements
    random.shuffle(self.seq)
    self.seq.sort()
    self.assertEqual(self.seq, list(range(10)))

    # should raise an exception for an immutable sequence
    self.assertRaises(TypeError, random.shuffle, (1,2,3))

  def test_choice(self):
    element = random.choice(self.seq)
    self.assertTrue(element in self.seq)

  def test_sample(self):
    with self.assertRaises(ValueError):
      random.sample(self.seq, 20)
    for element in random.sample(self.seq, 5):
      self.assertTrue(element in self.seq)


class TestSuite4(unittest.TestCase):
  """suite2 description"""

  def setUp(self):
    self.seq = list(range(10))

  @unittest.skip("demonstrating skipping")
  def test_skipped(self):
    self.fail("shouldn't happen")

  def test_shuffle(self):
    # make sure the shuffled sequence does not lose any elements
    random.shuffle(self.seq)
    self.seq.sort()
    self.assertEqual(self.seq, list(range(10)))

    # should raise an exception for an immutable sequence
    self.assertRaises(TypeError, random.shuffle, (1,2,3))

  def test_choice(self):
    element = random.choice(self.seq)
    self.assertTrue(element in self.seq)

  def test_sample(self):
    with self.assertRaises(ValueError):
      random.sample(self.seq, 20)
    for element in random.sample(self.seq, 5):
      self.assertTrue(element in self.seq)


class TestSuite5(unittest.TestCase):
  """suite2 description"""

  def setUp(self):
    self.seq = list(range(10))

  @unittest.skip("demonstrating skipping")
  def test_skipped(self):
    self.fail("shouldn't happen")

  def test_shuffle(self):
    # make sure the shuffled sequence does not lose any elements
    random.shuffle(self.seq)
    self.seq.sort()
    self.assertEqual(self.seq, list(range(10)))

    # should raise an exception for an immutable sequence
    self.assertRaises(TypeError, random.shuffle, (1,2,3))

  def test_choice(self):
    element = random.choice(self.seq)
    self.assertTrue(element in self.seq)

  def test_sample(self):
    with self.assertRaises(ValueError):
      random.sample(self.seq, 20)
    for element in random.sample(self.seq, 5):
      self.assertTrue(element in self.seq)

if __name__ == '__main__':
  with open('test-reports/unit.xml', 'w') as output:
    unittest.main(
      testRunner=xmlrunner.XMLTestRunner(output=output),
      failfast=False, buffer=False, catchbreak=False)
