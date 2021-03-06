# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def build(in_left, in_right):
            if in_left > in_right:
                return None
                
            val = postorder.pop()
            root = TreeNode(val)
            index = idx_map[val]
            root.right = build(index+1, in_right)
            root.left = build(in_left, index-1)
            return root
        
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return build(0, len(inorder) - 1)