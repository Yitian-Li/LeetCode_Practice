class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # i表示天数，k表示买入次数， j表示是否持股
        if not prices: return 0
        n = len(prices)
        dp = [[[0 for i in range(2)] for i in range(3)] for i in range(n)]
        for k in range(3):
            dp[0][k][1] = -float('inf')
            dp[-1][k][1] = -float('inf')

        for i in range(n):
            for k in range(1, 3):
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]) # 卖股票
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]) # 买股票

        return dp[n-1][2][0]