class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dp = [0]*n
        for i in range(1, n):
            dp[i] = max(dp[i-1] - prices[i-1] + prices[i], dp[i])
        return max(dp)