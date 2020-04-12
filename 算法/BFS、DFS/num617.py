# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None

        def dfs(t1, t2):
            if not t1 and not t2:
                return None

            val1 = t1.val if t1 else 0
            val2 = t2.val if t2 else 0
            left1 = t1.left if t1 else None
            left2 = t2.left if t2 else None
            right1 = t1.right if t1 else None
            right2 = t2.right if t2 else None

            node = TreeNode(val1 + val2)
            node.left = dfs(left1, left2)
            node.right = dfs(right1, right2)

            return node

        return dfs(t1, t2)