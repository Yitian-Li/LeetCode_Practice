class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        MinPrice = int(1e9)
        MaxProfit = 0
        for price in prices:
            MaxProfit = max(MaxProfit, price - MinPrice)
            MinPrice = min(MinPrice, price)
        return MaxProfit