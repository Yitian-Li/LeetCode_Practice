# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def bfs(queue):
            while queue:
                nxt = []
                res.append(queue[-1].val)

                for node in queue:
                    if node.left: nxt.append(node.left)
                    if node.right: nxt.append(node.right)
                queue = nxt
        
        if not root:
            return []
            
        res = []
        bfs([root])
        return res
