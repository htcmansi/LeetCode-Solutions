class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=0
        s=1
        max_profit=0
        while s<len(prices):
            curr=prices[s]-prices[b]
            if prices[b]<prices[s]:
                max_profit=max(curr,max_profit)
            else:
                b=s
            s +=1
        return max_profit
        