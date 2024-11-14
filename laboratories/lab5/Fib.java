import java.util.Arrays;

public class Fib {
  public int fib(int n) {
    if (n == 0 || n == 1)
      return n;

    int[] memo = new int[n + 1];
    Arrays.fill(memo, -1);

    memo[0] = 0;
    memo[1] = 1;

    return helper(n - 1, memo);
  }

  private static int helper(int i, int[] memo) {
    if (i < 2)
      return memo[i];
    if (memo[i] != -1)
      return memo[i];

    memo[i] = helper(i - 1, memo) + helper(i - 2, memo);

    return memo[i];
  }
}