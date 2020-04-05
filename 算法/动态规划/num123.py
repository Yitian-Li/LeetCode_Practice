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
        
        
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0

        n = len(prices)
        left = [0 for _ in range(n)] # 保存第i天最大利润
        right = [0 for _ in range(n)] 

        minprice = prices[0]
        for i in range(1, n):
            minprice = min(prices[i], minprice)
            left[i] = max(prices[i] - minprice, left[i-1])

        maxprice = prices[n-1]
        for j in range(n-2, -1, -1):
            maxprice = max(prices[j], maxprice)
            right[j] = max(maxprice - prices[j], right[j+1])

        res = left[n-1]
        for i in range(n-1):
            res = max(res, left[i]+right[i+1])
        return res