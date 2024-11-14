import java.util.Arrays;

class Solution {
    public int climbStairs(int n) {
        int[] memo = new int[n];
        Arrays.fill(memo, -1);

        int ret = helper(0, n, memo);

        System.out.println(Arrays.toString(memo));

        return ret;
    }

    public static int helper(int s, int end, int[] memo) {
        if (s == end)
            return 1;
        else if (s > end)
            return 0;
        else if (memo[s] != -1)
            return memo[s];

        memo[s] = helper(s + 1, end, memo) + helper(s + 2, end, memo);

        return memo[s];
    }

    public int minCostClimbingStairs(int[] cost) {
        int first = cost[0];
        int second = cost[1];

        if (cost.length <= 2)
            return Math.min(first, second);

        for (int i = 2; i < cost.length; i++) {
            int curr = cost[i] + Math.min(first, second);
            first = second;
            second = curr;
        }

        return Math.min(first, second);
    }

    public int coinChange(int[] coins, int amount) {
        int max_val = amount + 1;

        int[] memo = new int[max_val];
        Arrays.fill(memo, max_val);

        memo[0] = 0;

        for (int coin : coins) {
            for (int x = coin; x <= amount; x++) {
                memo[x] = Math.min(memo[x], memo[x - coin] + 1);
            }
            System.out.println(Arrays.toString(memo));
        }

        int ret = memo[amount] != max_val ? memo[amount] : -1;

        return ret;
    }

    public int rob(int[] nums) {
        int n = nums.length;
        int[] memo = new int[n + 1];

        if (n == 0)
            return 0;
        if (n == 1)
            return nums[0];

        memo[1] = nums[0];
        memo[2] = Math.max(nums[0], nums[1]);

        for (int i = 3; i <= n; i++) {
            memo[i] = Math.max(memo[i - 1], memo[i - 2] + nums[i - 1]);
        }

        System.out.println(Arrays.toString(memo));

        return memo[n];
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // 1.
        // int test = 9;
        // System.out.println(s.climbStairs(test));

        // 2.
        // int[] test = { 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 3 };
        // System.out.println(s.minCostClimbingStairs(test));

        // 3.
        // int[] coins = { 2 };
        // int amount = 3;
        // System.out.println(s.coinChange(coins, amount));

        // 4.
        int[] test = { 2, 7, 9, 3, 1 };
        System.out.println(s.rob(test));
    }
}