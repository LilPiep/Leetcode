class Solution {
    int count = 0;
    
    Pair<Integer, Integer> postOrder(TreeNode root) {
        if (root == null) {
            return new Pair(0, 0);
        }
        
        Pair<Integer, Integer> left = postOrder(root.left);
        Pair<Integer, Integer> right = postOrder(root.right);
        
        int nodeSum = left.getKey() + right.getKey() + root.val;
        int nodeCount = left.getValue() + right.getValue() + 1;

        if (root.val == nodeSum / (nodeCount)) {
            count++;
        }
        
        // Return the sum of nodes and the count in the subtree.
        return new Pair(nodeSum, nodeCount);
    }
    
    public int averageOfSubtree(TreeNode root) {
        postOrder(root);
        return count;
    }
}