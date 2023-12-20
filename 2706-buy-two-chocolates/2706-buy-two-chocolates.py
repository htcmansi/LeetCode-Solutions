class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        left_money=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                left_money = money - (prices[0] + prices[1])
                if left_money>=0:
                    return left_money        
        return money