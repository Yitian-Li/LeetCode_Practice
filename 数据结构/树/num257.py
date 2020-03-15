# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        def dfs(root, path):
            if not root:
                return
            elif not(root.left or root.right):
                path += str(root.val)
                paths.append(path)
                return
            else:
                path += str(root.val) + "->"
                dfs(root.left, path)
                dfs(root.right, path)

        path = ""
        dfs(root, path)
        return paths