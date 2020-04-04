class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0
        # dp[i][0] 持有股票
        # dp[i][1] 不持股，因为之前卖了
        # dp[i][2] 不持股，因为今天卖了
        n = len(prices)
        dp = [[0, 0, 0] for _ in range(n)]

        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][2], dp[i-1][1])
            dp[i][2] = dp[i-1][0]+prices[i]
        
        return max(dp[n-1])