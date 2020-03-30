# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        def tolist(root):
            insert = root.left
            p = root.left
            while(p.right):
                p = p.right
            p.right = root.right

            root.left = None
            root.right = insert
        
        while(root):
            if root.left:
                tolist(root)
            root = root.right