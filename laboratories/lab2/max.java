import java.util.*;

public class max {
  public int find_max(int[] nums) {
    if (nums.length == 1) {
      return nums[0];
    }
    int mid = nums.length / 2;
    int[] left_array = Arrays.copyOfRange(nums, 0, mid);
    int[] right_array = Arrays.copyOfRange(nums, mid, nums.length);

    int l = find_max((left_array));
    int r = find_max((right_array));

    if (l > r) {
      return l;
    } else {
      return r;
    }
  }

  public static void main(String[] args) {
    max obj = new max();
    int[] test = { 1, 2, 1, 4, 1 };

    System.out.println(obj.find_max(test));
  }
}
