import unittest
from fib import Solution

obj = Solution()
class Tester(unittest.TestCase):
  
  def test1(self):
    self.assertEqual(obj.fib(4), 2)
  def test2(self):
    self.assertEqual(obj.fib(11), 55)
  def test3(self):
    self.assertEqual(obj.fib(13), 144)
  def test4(self):
    self.assertEqual(obj.fib(17), 987)
  def test5(self):
    self.assertEqual(obj.fib(21), 6765)

# python -m unittest test.Tester