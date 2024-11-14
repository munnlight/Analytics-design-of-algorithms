class Solution():
  def minCost(self, k):
    n = len(k)
    power = 1
    layer = 1
    cost = 0
    for i in range(1, n + 1):
      holder = k[n - i]
      if i <= power:
        cost += layer * holder
      else:
        power += power * 2
        layer += 1
        cost += layer * holder

    return cost

if __name__ == "__main__":
  k = [11, 17, 25, 35]

  c = Solution()
  print(c.minCost(k))


