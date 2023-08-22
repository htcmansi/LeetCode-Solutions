class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n=len(candies)
        max_candies = max(candies)
        candie=[]
        for i in range(n):
            if candies[i] + extraCandies >= max_candies:
                candie.append(True)
            else:
                candie.append(False)
        return candie
        