# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Check if a two nodes have same values, same left child and right child
    def verifNode(self, node1, node2):
        if node1.val != node2.val:
            return False
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return True
        
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        return (self.verifNode(p, q) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
            