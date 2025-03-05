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
    public int RangeSumBST(TreeNode root, int low, int high) {
        Stack<TreeNode> s = new Stack<TreeNode>();
        s.Push(root);
        int ans = 0;

        while (s.Count > 0){
            TreeNode node = s.Pop();
            if ((node.val >= low) & (node.val <= high)){
                ans += node.val;
            }
            if (node.left != null) {
                s.Push(node.left);
            }
            if (node.right != null) {
                s.Push(node.right);
            }
        }
        return ans;
    }
}