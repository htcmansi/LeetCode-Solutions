class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        m=set(candyType)
        n=len(candyType)
        max_candy=min(len(m),n//2)
        return max_candy