# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        def getAncestors(root, node, path, ancestors):
            if root == node:
                path.append(root)
                ancestors.append(path)
                return
            
            if root.left:
                path.append(root)
                getAncestors(root.left, node, path[:], ancestors)
                path.pop()

            if root.right:
                path.append(root)
                getAncestors(root.right, node, path[:], ancestors)
                path.pop()

        p_ancestors, q_ancestors = [], []
        getAncestors(root, p, [], p_ancestors)
        getAncestors(root, q, [], q_ancestors)

        p_ancestors = p_ancestors[0]
        q_ancestors = q_ancestors[0]

        depth = min(len(p_ancestors), len(q_ancestors)) - 1
        
        while depth >= 0:
            if p_ancestors[depth] == q_ancestors[depth]:
                return p_ancestors[depth]
            depth -= 1
            
            
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def dfs(node, p, q):
            if not node:
                return False

            mid = node == p or node == q
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)
            if mid + left + right > 1:
                self.ans = node

            return mid or left or right
                
        dfs(root, p, q)
        return self.ans