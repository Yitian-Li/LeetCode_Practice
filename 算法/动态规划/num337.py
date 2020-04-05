# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        

        def goRob(root):
            if not root:
                return [0, 0]

            # cash[0]代表不偷，cash[1]代表偷
            cash = [0, 0]

            left = goRob(root.left)
            right = goRob(root.right)

            cash[0] = max(left) + max(right)
            cash[1] = root.val + left[0] + right[0]

            return cash

        return max(goRob(root))