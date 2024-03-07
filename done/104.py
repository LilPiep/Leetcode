class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root) -> int:
    count = 1
    if not root:
        count -= 1
        return count
    else:
        return count + max(maxDepth(root.left), maxDepth(root.right))
