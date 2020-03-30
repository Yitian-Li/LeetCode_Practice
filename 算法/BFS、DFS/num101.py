# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        nodes = [root]
        flag = True
        while flag:
            child = []
            for node in nodes:
                if node:
                    child.append(node.left)
                    child.append(node.right)
                else:
                    child.append(None)
                    child.append(None)
            nodes = child
            ans, flag = self.helper(nodes)
            if not ans:
                return False
        return True

    def helper(self, nodes):
        flag = False
        nums = []
        for n in nodes:
            if not n:
                nums.append(None)
            else:
                flag = True
                nums.append(n.val)

        if nums[:] == nums[::-1]:
            return True, flag
        else:
            return False, flag
