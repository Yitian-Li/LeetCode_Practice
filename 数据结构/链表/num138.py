"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}

        def copy_helper(p):
            if not p:
                return None

            # 如果此前已经根据p构建了一个new_node,那么不需要再构建
            if p in visited:
                return visited[p]

            # 根据p构建new_node并保存p->new_node的键值对
            new_node = Node(p.val)
            visited[p] = new_node

            new_node.next = copy_helper(p.next)
            new_node.random = copy_helper(p.random)
            return new_node

        res = copy_helper(head)

        return res
