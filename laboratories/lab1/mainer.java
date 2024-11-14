package lab1;

import java.util.*;

public class mainer {
  public static void main(String[] args) {
    int[] test = { -1, 0, 1, 2, -1, -4 };

    Solution s = new Solution();
    List<List<Integer>> result = s.threeSum(test);

    System.out.println(result);
  }
}
