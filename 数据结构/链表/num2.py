# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p, q = l1, l2
        carry, cur = 0, 0
        head = ListNode(0)
        res = head

        while p and q:
            cur = p.val + q.val + carry
            if cur >= 10:
                carry = 1
                cur -= 10
            else:
                carry = 0
            new_node = ListNode(cur)
            res.next = new_node
            res = res.next
            p = p.next
            q = q.next

        t = p if p else q

        while t:
            cur = t.val + carry
            if cur >= 10:
                carry = 1
                cur -= 10
            else:
                carry = 0
            new_node = ListNode(cur)
            res.next = new_node
            res = res.next
            t = t.next

        if carry == 1:
            new_node = ListNode(carry)
            res.next = new_node

        return head.next
