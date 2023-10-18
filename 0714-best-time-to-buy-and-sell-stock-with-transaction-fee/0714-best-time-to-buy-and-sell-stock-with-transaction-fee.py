class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        buy = prices[0] + fee  
        for p in prices:
            if p < buy:
                buy = p  
            elif p > buy + fee:
                profit += p - buy - fee  
                buy = p - fee  
        return profit