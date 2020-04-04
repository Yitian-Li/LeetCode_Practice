# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def helper(root, s):
            if root is None: return s + 'None,'
            s = s + str(root.val) + ','
            s = helper(root.left, s)
            s = helper(root.right, s)
            return s

        return helper(root, "")        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')

        def helper(l):
            node = l.pop(0)
            if node == 'None': 
                return None
            root = TreeNode(int(node))
            root.left = helper(l)
            root.right = helper(l)
            return root

        return helper(data)
            

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))