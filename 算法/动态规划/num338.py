class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0] * (num+1)
        for i in range(num+1):
            if i % 2:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i//2]
        return dp
