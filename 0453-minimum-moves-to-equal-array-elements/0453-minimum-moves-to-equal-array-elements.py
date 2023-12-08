class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=0
        nums.sort()
        for i in range(len(nums)):
            m +=nums[i]-nums[0]
        return m