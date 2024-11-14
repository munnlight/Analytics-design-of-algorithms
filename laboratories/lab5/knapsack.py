class Solution(object):
  def maxVal(self, v, w, bag_size):
    memo = [-1] * (max(w) + 1)

    return bag_size
  
  def helper(self, i, w, v, memo):
    if i < 1:
      return -1
    if memo[i] != -1:
      return memo[i]
    
    max_per = -1

    return memo[w]

v = [1, 2, 3, 5]
w = [1, 1, 3, 2]
bag_size = 7

v = [1, 2]
w = [1, 1]
bag_size = 1

c = Solution()
print(c.maxVal(v, w, bag_size))


