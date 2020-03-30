# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        nodes = [root]
        bfs = []
        while(nodes):
            vals = []
            nxt_nodes = []
            for n in nodes:
                if not n:
                    continue
                if n.left:
                    nxt_nodes.append(n.left)
                if n.right:
                    nxt_nodes.append(n.right)
                vals.append(n.val)
            bfs.append(vals)
            nodes = nxt_nodes

        return bfs