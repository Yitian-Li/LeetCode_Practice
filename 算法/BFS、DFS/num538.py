# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.num = 0
        
        def dfs(root):
            if root is None:
                return 
            else:
                dfs(root.right)
                self.num = self.num + root.val
                root.val = self.num
                dfs(root.left)
                return root

        return dfs(root)