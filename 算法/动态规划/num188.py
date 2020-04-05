class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        max_k = k
        # dp[i][k][j] 天数|买入次数|持股
        if not prices: return 0
        n = len(prices)
        if max_k > n//2:
            dp = [[0, 0] for _ in range(n)]
            dp[0][1] = float('-inf')
            dp[-1][1] = float('-inf')

            for i in range(n):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            return dp[-1][0]

        else:
            dp = [[[0, 0] for _ in range(max_k+1)] for _ in range(n)]
            # 没有开始交易，初始化
            for k in range(max_k, 0, -1):
                dp[0][k][1] = float('-inf')
                dp[-1][k][1] = float('-inf')

            for i in range(n):
                for k in range(1, max_k+1):
                    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]) # 昨天就卖了，或者今天卖的
                    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]) # 昨天就买了，或者今天刚买的
            
            return dp[-1][-1][0]