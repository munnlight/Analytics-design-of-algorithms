import unittest
import json
import os

def merge(arr):
  if len(arr) > 1:
    mid = len(arr) // 2 
    L = arr[:mid]       
    R = arr[mid:]

    l = merge(L)      
    r = merge(R) 
    
    if l > r:
      return l
    else:
      return r
    
  return arr



dir = os.path.dirname(os.path.realpath(__file__))
path = dir + '/test_cases_max.txt'
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
    self.assertEqual(merge(to_solve[0]), solved[0])
  def test2(self):
    self.assertEqual(merge(to_solve[1]), solved[1])
  def test3(self):
    self.assertEqual(merge(to_solve[2]), solved[2])
  def test4(self):
    self.assertEqual(merge(to_solve[3]), solved[3])
  def test5(self):
    self.assertEqual(merge(to_solve[4]), solved[4])


if __name__ == '__main__':
  unittest.main()