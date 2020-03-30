# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_lv = 0
        if not root:
            return max_lv
            
        nodes = [root]
        while(nodes):
            nxt_nodes = []
            for n in nodes:
                if not n:
                    continue
                if n.left:
                    nxt_nodes.append(n.left)
                if n.right:
                    nxt_nodes.append(n.right)
            nodes = nxt_nodes
            max_lv += 1

        return max_lv