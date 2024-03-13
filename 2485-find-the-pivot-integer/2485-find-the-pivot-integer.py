class Solution:
    def pivotInteger(self, n: int) -> int:
        totalSum=sum(range(1, n + 1))
        left= 0
        for x in range(1, n + 1):
            left += x
            right=totalSum - left+x
            if left==right:
                return x
        return -1