# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        queue = [root]
        while queue:
            node = queue.pop()
            node.left, node.right = node.right, node.left
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        return root
        
        
class Solution(object):
	def invertTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""

		if not root:
			return None
		# 将当前节点的左右子树交换
		root.left,root.right = root.right,root.left
		
		self.invertTree(root.left)
		self.invertTree(root.right)
		
		return root
