# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValid(node, low, up):
            if not node:
                return True
            if node.val <= low or node.val >= up:
                return False
            if not isValid(node.left, low, node.val) or not isValid(node.right, node.val, up):
                return False
            return True

        up = float('inf')
        low = float('-inf')
        return isValid(root, low, up)

