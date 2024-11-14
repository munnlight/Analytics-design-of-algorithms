class TreeNode {
  Integer value = null;
  TreeNode left;
  TreeNode right;

  TreeNode(int value) {
    this.value = value;
    left = null;
    right = null;
  }
}

public class BinaryTree {
  TreeNode root;

  BinaryTree() {
    root = null;
  }

  public void insert(int value) {
    root = insertRec(root, value);
  }

  private TreeNode insertRec(TreeNode root, int value) {

    if (root == null) {
      root = new TreeNode(value);
      return root;
    }

    if (value < root.value) {
      root.left = insertRec(root.left, value);
    } else if (value > root.value) {
      root.right = insertRec(root.right, value);
    }

    return root;
  }

  public void inOrder() {
    inOrderRec(root);
    System.out.println("");
  }

  private void inOrderRec(TreeNode root) {
    if (root != null) {
      inOrderRec(root.left);
      System.out.print(root.value + " ");
      inOrderRec(root.right);
    }
  }

  public void search(int find) {
    boolean isThere = searchRec(root, find);
    if (isThere) {
      System.out.println(find + " is there");
    } else {
      System.out.println(find + " is not there");
    }
  }

  private boolean searchRec(TreeNode node, int find) {
    if (node.value == null) {
      return false;
    }
    if (node.value == find) {
      return true;
    }

    if (node.value < find) {
      if (node.right != null) {
        return searchRec(node.right, find);
      }
      return false;
    } else if (node.value > find) {
      if (node.left != null) {
        return searchRec(node.left, find);
      }
      return false;
    }
    return false;

  }

  public static void main(String[] args) {
    BinaryTree tree = new BinaryTree();

    int[] nums = { 10, 9, 2, 3, 4, 11, 32, 12 };

    for (int i = 0; i < nums.length; i++) {
      tree.insert(nums[i]);
    }

    tree.inOrder();

    tree.search(12);
  }
}
