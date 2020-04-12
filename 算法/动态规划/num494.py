class Solution(object):
    def findTargetSumWays(self, nums, S):
        Sum = sum(nums)
        if abs(S) > Sum:
            return 0

        dp = [[0] * (2 * Sum + 1) for _ in range(len(nums))]
        dp[0][nums[0] + Sum] += 1
        dp[0][-nums[0] + Sum] += 1

        for i in range(1, len(nums)):
            for j in range(-Sum, Sum + 1):
                if 0 <= j - nums[i] + Sum < (2 * Sum + 1):
                    dp[i][j + Sum - nums[i]] += dp[i - 1][j + Sum]
                if 0 <= j + nums[i] + Sum < (2 * Sum + 1):
                    dp[i][j + Sum + nums[i]] += dp[i - 1][j + Sum]

        return dp[-1][S + Sum]