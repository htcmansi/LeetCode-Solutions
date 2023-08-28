class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        con=0
        max_count=0
        for i in range(len(nums)):
            if nums[i] == 1:
                con +=1
                max_count=max(max_count,con)
            else:
                con=0
        return max_count