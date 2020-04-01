# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        setA = set()
        p, q = headA, headB
        while p:
            if not p in setA:
                setA.add(p)
            p = p.next

        while q:
            if q in setA:
                break
            q = q.next

        return q