public class Solution {
    public int GoodNodes(TreeNode root) {
        Stack<(TreeNode, int)> s = new Stack<(TreeNode, int)>();
        s.Push((root, root.val));
        int ans = 0;

        while(s.Count != 0){
            (TreeNode node, int maxVal) = s.Pop();
            
            if(node.val >= maxVal){
                ans += 1;
                maxVal = node.val;
            }

            if (node.right != null){
                s.Push((node.right, maxVal));
            }
            if (node.left != null){
                s.Push((node.left, maxVal));
            }
        }

        return ans;
    }
}