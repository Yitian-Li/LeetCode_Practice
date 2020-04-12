# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0

        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def dfs(self, root, target):
        cnt = 0
        if not root:
            return 0
        if root.val == target:
            cnt += 1

        cnt += self.dfs(root.left, target - root.val)
        cnt += self.dfs(root.right, target - root.val)

        return cnt