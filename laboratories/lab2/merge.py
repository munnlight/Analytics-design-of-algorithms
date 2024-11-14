import unittest
import json
import os

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 
        L = arr[:mid]       
        R = arr[mid:]

        merge_sort(L)        
        merge_sort(R)        

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

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
    self.assertEqual(merge_sort(to_solve[0]), solved[0])
  def test2(self):
    self.assertEqual(merge_sort(to_solve[1]), solved[1])
  def test3(self):
    self.assertEqual(merge_sort(to_solve[2]), solved[2])
  def test4(self):
    self.assertEqual(merge_sort(to_solve[3]), solved[3])
  def test5(self):
    self.assertEqual(merge_sort(to_solve[4]), solved[4])


if __name__ == "__main__":
    unittest.main()
