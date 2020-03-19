# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder:
            root = TreeNode(preorder.pop(0))
            l, r = [], []
            for i in preorder:
                if i <= root.val:
                    l += [i]
                else:
                    r += [i]
            root.left = self.bstFromPreorder(l)
            root.right = self.bstFromPreorder(r)
            return root