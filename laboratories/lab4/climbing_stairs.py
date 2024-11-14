class Solution:
    def climbStairs(self, n):
        dp = [-1] * (n + 1)
        return self.solve(0, n, dp)

    def solve(self, i, n, dp):
        if i == n:
            return 1
        if i > n:
            return 0

        if dp[i] != -1:
            return dp[i]

        dp[i] = self.solve(i + 1, n, dp) + self.solve(i + 2, n, dp)

        return dp[i]

c = Solution()
c.climbStairs(4)