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
    public int MaxLevelSum(TreeNode root) {
        Queue<TreeNode> queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        int best_sum = 0;
        int level_best = 0;
        int level = -1;

        while (queue.Count > 0) {
            int currentLength = queue.Count;
            int level_sum = 0;
            level++;

            for (int i = 0; i < currentLength; i++) {
                TreeNode node = queue.Dequeue();
                level_sum += node.val;
                if (node.left != null) {
                    queue.Enqueue(node.left);
                }
                if (node.right != null) {
                    queue.Enqueue(node.right);
                }
            }
            if(level_sum > best_sum){
                best_sum = level_sum;
                level_best = level;
            }
        }

        return level;
    }
}