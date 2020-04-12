from collections import deque
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        n = len(nums)

        cur = nums[-1]
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2

        dp = [[False] * (target + 1) for _ in range(n)]

        for i in range(n):
            for j in range(target+1):
                if nums[i] == target:
                    return True
                if nums[i] == j:
                    dp[i][j] = True

        for i in range(1, n):
            for j in range(target + 1):
                if dp[i - 1][j] or dp[i - 1][j - nums[i]]:
                    dp[i][j] = True

            if dp[i][target] == True:
                return True

        return False
