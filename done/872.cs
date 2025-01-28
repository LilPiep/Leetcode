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
    public void dfs(TreeNode node, List<int> leafValues) {
        if (node != null) {
            if (node.left == null && node.right == null)
                leafValues.Add(node.val);
            dfs(node.left, leafValues);
            dfs(node.right, leafValues);
        }
    }

    public bool LeafSimilar(TreeNode root1, TreeNode root2) {
        List<int> leaves1 = new List<int>();
        List<int> leaves2 = new List<int>();
        dfs(root1, leaves1);
        dfs(root2, leaves2);
        return leaves1.SequenceEqual(leaves2);
    }
}