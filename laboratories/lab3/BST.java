import java.util.Arrays;

public class BST {
  public TreeNode sortedArrayToBST(int[] nums) {
    if (nums.length > 1) {
      int mid = nums.length / 2;
      TreeNode node1 = sortedArrayToBST(Arrays.copyOfRange(nums, 0, mid));
      TreeNode node2 = sortedArrayToBST(Arrays.copyOfRange(nums, mid, nums.length));

      TreeNode node = TreeNode(nums[mid]);
      node.right = node2;
      node.left = node1;

      return node;
    } else {
      return new TreeNode(nums[0]);
    }
  }

  public static void main(String[] args) {

  }
}
