class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        prev = 0
        for i in flowerbed:
            if i == 1:
                if prev == 1: 
                    count -= 1
                prev = 1
            elif prev == 1:
                    prev = 0 
            else:
                count += 1
                prev = 1 
        return count >= n
        