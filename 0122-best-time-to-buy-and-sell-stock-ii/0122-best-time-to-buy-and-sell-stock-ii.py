class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """buy=0
        sell=1
        max_profit=0
        while sell<len(prices):
            current=prices[sell]-prices[buy]
            if prices[buy]<prices[sell]:
                max_profit +=(current)
            buy +=1
            sell +=1
        return max_profit"""
        profit=0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                profit += prices[i+1]-prices[i]
        return profit
            