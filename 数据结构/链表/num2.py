# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        val1, val2, cnt = 0, 0, 0
        while p1:
            val1 += p1.val * (10**cnt)
            p1, cnt = p1.next, cnt+1
        cnt = 0
        while p2:
            val2 += p2.val * (10**cnt)
            p2, cnt = p2.next, cnt+1
        res = val1 + val2
        if res == 0:
            return ListNode(0)

        p = voidhead = ListNode(None)
        while res:
            insert = ListNode(res % 10)
            p.next = insert
            p = p.next
            res = res // 10
        return voidhead.next