class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        # dp[i][0]持股的总现金，dp[i][1]不持股的总现金
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][0]+prices[i], dp[i-1][1])
 
        return max(dp[n-1])