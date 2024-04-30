package leetcode.easy;

public class ConvertSortedArrayToBinarySearchTree {

    public static void main(String[] args) {
        System.out.println(sortedArrayToBST(new int[] {-10,-3,0,5,9}));
        System.out.println(sortedArrayToBST(new int[] {1,3}));
    }

    public static TreeNode sortedArrayToBST(int[] nums) {
        if (nums == null || nums.length == 0) {
            return null;
        }
        return makeBST(nums, 0, nums.length - 1);
    }

    public static TreeNode makeBST(int[] nums, int low, int high) {
        if (low > high) {
            return null;
        }

        int mid = (high + low) / 2;

        TreeNode node = new TreeNode(nums[mid]);
        node.left = makeBST(nums, low, mid - 1);
        node.right = makeBST(nums, mid + 1, high);

        return node;
    }


    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }

        @Override
        public String toString() {
            return "TreeNode{" +
                    "val=" + val +
                    ", left=" + left +
                    ", right=" + right +
                    '}';
        }
    }
}
