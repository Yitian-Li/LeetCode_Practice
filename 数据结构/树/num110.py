# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return not self.dfs(root)==-1

    def dfs(self, root):
        if not root: return 0
        left = self.dfs(root.left)
        if left==-1: return -1 
        right = self.dfs(root.right)
        if right==-1: return -1
        return 1 + max(left,right) if abs(left-right) < 2 else -1
