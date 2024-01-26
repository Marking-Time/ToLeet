import unittest
from main import sum
from main import to_roman

class TestSum(unittest.TestCase):
  def test_list_init(self):
    """
    Test that it can sum a list of integers
    """
    data = [1, 2, 3]
    result = sum(data)
    self.assertEqual(result, 6)

class TestRoman(unittest.TestCase):
  def test_tens(self):
    """
    Test that it can convert a number to roman numerals
    """
    data = ['12']
    result = to_roman(data)
    self.assertEqual(result, ['XII'])

  def test_ones(self):
    data = ['9']
    result = to_roman(data)
    self.assertEqual(result, ['IX'])

  def test_hundreds(self):
    data = ["111"]
    result = to_roman(data)
    self.assertEqual(result, ["CXI"])

  def test_thousands(self):
    data = ["10000"]
    result = to_roman(data)
    self.assertEqual(result, ['10xM'])
    
    

if __name__ == '__main__':
  unittest.main()
    
