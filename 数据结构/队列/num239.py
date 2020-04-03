from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # base case
        n = len(nums)
        if n * k == 0: return []
        if k == 1: return nums

        def update_deq(i):
            if deq and deq[0] == i - k:
                deq.popleft()

            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            deq.append(i)
        
        deq = deque()
        max_idx = 0
        for i in range(k):
            update_deq(i)
            if nums[i] > nums[max_idx]:
                max_idx = i
        ans = [nums[max_idx]]

        for i in range(k, n):
            update_deq(i)
            ans.append(nums[deq[0]])
        return ans