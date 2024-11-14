import unittest
import os 
import json

dir = os.path.dirname(os.path.realpath(__file__))
path = dir + '/test_cases.txt'
to_solve = []
solved = []

with (open(path, 'r')) as file:
  lines = file.read()
  tests = lines.split('?')
  for test in tests:
    x, y = test.split(';')
    to_solve.append(json.loads(x))
    solved.append(json.loads(y))


class TestSortMethods(unittest.TestCase):
  def test1(self):
    self.assertEqual(insertion_sort(to_solve[0]), solved[0])
  def test2(self):
    self.assertEqual(insertion_sort(to_solve[1]), solved[1])
  def test3(self):
    self.assertEqual(insertion_sort(to_solve[2]), solved[2])
  def test4(self):
    self.assertEqual(insertion_sort(to_solve[3]), solved[3])
  def test5(self):
    self.assertEqual(insertion_sort(to_solve[4]), solved[4])

def insertion_sort(nums):
  for i in range(1, len(nums)):
    key = nums[i]
    j = i - 1
    while j >= 0 and nums[j] > key:
      nums[j + 1] = nums[j]
      j -= 1
    
    nums[j + 1] = key

  return nums

if __name__ == '__main__':
  unittest.main()