class Solution():
  def maxProfit(self, prices: int) -> int:
    n = len(prices)
    memo = [[-1] * (2) for _ in range(n + 1)]

    memo[n][0] = memo[n][1] = 0

    for i in range(n - 1, -1, -1):
      for buy in range(2):
        profit = 0
        if buy:
          profit = max((-prices[i] + memo[i + 1][0]), memo[i + 1][1])
        else:
          profit = max((prices[i] + memo[i + 1][1]), memo[i + 1][0])
        
        memo[i][buy] = profit

    return memo[0][1]
    
  def numTrees(self, n):
      memo = [0] * (n + 1)
      memo[0] = 1

      for i in range(1, n + 1):
          sum = 0
          for j in range(0, i):
              sum += memo[j] * memo[i - j - 1]

          memo[i] = sum
      
      return memo[n]
  
if __name__ == "__main__":
  s = Solution()
  # memp = s.maxProfit([1, 2, 3, 4, 5])
  # memp[1][1] = 5
  # print(memp)

  print(s.numTrees(5))

