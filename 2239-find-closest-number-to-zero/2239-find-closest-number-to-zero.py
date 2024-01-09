class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        num=float('inf')
        nums.sort()
        for i in nums:
            if abs(i)<=num:
                num=abs(i)
                c=i
        return c
