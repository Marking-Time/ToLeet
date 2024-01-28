import unittest
from main import to_roman

class TestRoman(unittest.TestCase):

  def test_ones(self):
    data = ['1']
    result = to_roman(data)
    self.assertEqual(result, ['I'])


if __name__ == '__main__':
  unittest.main()