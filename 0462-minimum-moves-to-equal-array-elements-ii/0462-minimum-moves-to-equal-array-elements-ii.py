class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        m=0
        nums.sort()
        mid=nums[len(nums)//2]
        for i in range(len(nums)):
            m +=abs(mid-nums[i])
        return m

           