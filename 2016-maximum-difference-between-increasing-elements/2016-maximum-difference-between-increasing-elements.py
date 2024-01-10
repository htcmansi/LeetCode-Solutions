class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diff=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    res=nums[j]-nums[i]
                    diff=max(diff,res)
        if diff==0:
            return -1
        return diff