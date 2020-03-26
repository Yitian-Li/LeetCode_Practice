class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]

        dp = [0] * size
        dp[0] = nums[0]
        for i in range(1, size):
            dp[i] = max(dp[i-1], 0) + nums[i]

        return max(dp)