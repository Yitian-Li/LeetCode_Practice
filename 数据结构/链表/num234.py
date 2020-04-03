# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow

        if mid == mid.next:
            p = mid.next.next
        else:
            p = mid.next

        q = self.reverseList(p)
        p = head
        while p and q:
            if p.val == q.val:
                p = p.next
                q = q.next
            else:
                return False

        return True

    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre