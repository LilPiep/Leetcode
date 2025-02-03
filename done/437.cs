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
    public int PathSum(TreeNode root, int targetSum) {
        if(root == null) return 0;

        return Dfs(root, targetSum) 
            + PathSum(root.left, targetSum)
            + PathSum(root.right, targetSum);
        
        int Dfs(TreeNode node, long sum)
        {
            var s = node.val == sum ? 1 : 0;

            if(node.left != null)
                s += Dfs(node.left, sum-node.val);

            if(node.right != null)
                s += Dfs(node.right, sum-node.val);

            return s;
        }
    }
}