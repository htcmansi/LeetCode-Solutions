class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sort_piles=sorted(piles,reverse=True)
        n=len(sort_piles)//3
        coins=0
        for i in range(n):
            coins+=(sort_piles[2*i+1])
        return coins