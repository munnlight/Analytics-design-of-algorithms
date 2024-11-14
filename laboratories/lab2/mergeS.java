import java.util.*;

class mergeS {
  public int[] sortArray(int[] nums) {
    merge_sort(nums);
    return nums;
  }

  public static void merge_sort(int[] nums) {
    if (nums.length > 1) {
      int mid = nums.length / 2;
      int[] left = Arrays.copyOfRange(nums, 0, mid);
      int[] right = Arrays.copyOfRange(nums, mid, nums.length);

      merge_sort(left);
      merge_sort(right);

      int i = 0;
      int j = 0;
      int k = 0;

      while (i < left.length && j < right.length) {
        if (left[i] <= right[j]) {
          nums[k] = left[i];
          i++;
        } else {
          nums[k] = right[j];
          j++;
        }
        k++;
      }

      while (i < left.length) {
        nums[k] = left[i];
        i++;
        k++;
      }

      while (j < right.length) {
        nums[k] = right[j];
        j++;
        k++;
      }
    }
  }
}
