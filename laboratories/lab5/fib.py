# from test import Tester

class Solution(object):
  memo = []
  memo.append(0)
  memo.append(1)

  def fib(self, n, memo):
    if n < 2:
      return n
    
    return self.fib(n - 1, memo) + self.fib
  
