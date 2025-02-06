/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    int bestDepth = 0;

    private void ZigZag(TreeNode node, bool goLeft, int steps){
        if (node == null) {
            return;
        }
        bestDepth = Math.Max(bestDepth, steps);
        if (goLeft) {
            ZigZag(node.left, false, steps + 1);
            ZigZag(node.right, true, 1);
        } else {
            ZigZag(node.left, false, 1);
            ZigZag(node.right, true, steps + 1);
        }
    }

    public int LongestZigZag(TreeNode root) {
        ZigZag(root,true,0);
        return bestDepth;
    }
}