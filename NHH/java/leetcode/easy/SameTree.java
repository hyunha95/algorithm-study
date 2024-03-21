package leetcode.easy;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class SameTree {

    private List<Integer> pList = null;
    private List<Integer> qList = null;

    public boolean isSameTree(TreeNode p, TreeNode q) {
        pList = new ArrayList<>();
        qList = new ArrayList<>();

        preOrder(p, pList);
        preOrder(q, qList);

        if (pList.size() != qList.size()) {
            return false;
        }

        for (int i = 0; i < pList.size(); i++) {
            if (!Objects.equals(pList.get(i), qList.get(i))) {
                return false;
            }
        }

        return true;
    }

    private void preOrder(TreeNode node, List<Integer> list) {
        if (node != null) {
            list.add(node.val);
            preOrder(node.left, list);
            preOrder(node.right, list);
        } else {
            list.add(null);
        }
    }


    public class TreeNode {
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
    }

}
