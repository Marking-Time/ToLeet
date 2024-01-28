import unittest
from main import to_roman

class TestRoman(unittest.TestCase):

  def test_ones(self):
    data = ['1']
    result = to_roman(data)
    self.assertEqual(result, 'I')

  def test_tens(self):
    data = ['11']
    result = to_roman(data)
    self.assertEqual(result, 'XI')

  def test_hundreds(self):
    data = ['100']
    result = to_roman(data)
    self.assertEqual(result, 'C')


if __name__ == '__main__':
  unittest.main()