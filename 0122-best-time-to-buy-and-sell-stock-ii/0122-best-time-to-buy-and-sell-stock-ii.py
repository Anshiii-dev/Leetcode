class Solution(object):
    def maxProfit(self, prices):
        buy=prices[0]
        sell=0
        max_profit=0
        profit=0
        for i in range(1,len(prices)):
         if prices[i]>prices[i-1]:
            max_profit+=prices[i]-prices[i-1]
        return max_profit+profit