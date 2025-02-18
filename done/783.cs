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

    int ans = int.MaxValue;
    private TreeNode prev = null;

    public int MinDiffInBST(TreeNode root) {
        InOrder(root);
        return ans;
    }

    private void InOrder(TreeNode node) {
        if (node == null) return;
        InOrder(node.left);
        if (prev != null) {
            ans = Math.Min(ans, node.val - prev.val);
        }
        prev = node;
        InOrder(node.right);
    }
}