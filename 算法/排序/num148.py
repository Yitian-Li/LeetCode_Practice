# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        slow, fast = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow, None
        left, right = self.sortList(head), self.sortList(mid)

        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, right.next
            else:
                h.next, right = right, right.next
            h = h.next
        
        h.next = left if left else right
        return res.next
        




class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h = head
        length = 0
        intv = 1
        while h:
            h = h.next
            length += 1
        res = ListNode(None)
        res.next = head
        # merge the list in different intv.
        while intv < length:
            pre = res
            h = res.next
            while h:
                # get the two merge head `h1`, `h2`
                h1 = h
                i = intv
                while i and h:
                    h = h.next
                    i -= 1
                # no need to merge because the `h2` is None.
                if i:
                    break 
                h2 = h
                i = intv
                while i and h:
                    h = h.next
                    i -= 1
                # the `c2`: length of `h2` can be small than the `intv`.
                c1 = intv
                c2 = intv - i
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next = h1
                        h1 = h1.next
                        c1 -= 1
                    else:
                        pre.next = h2
                        h2 = h2.next
                        c2 -= 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre = pre.next
                    c1 -= 1
                    c2 -= 1
                pre.next = h 
            intv *= 2
        return res.next