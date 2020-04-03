class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        left = [0]*n
        right = [0]*n

        left[0] = 1
        right[n-1] = 1

        ans = [0]*n

        for i in range(1, n):
            left[i] = left[i-1]*nums[i-1]
            right[n-i-1] = right[n-i]*nums[n-i]

        for i in range(n):
            ans[i] = left[i] * right[i]

        return ans