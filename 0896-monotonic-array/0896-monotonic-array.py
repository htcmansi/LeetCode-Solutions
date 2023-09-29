class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase=decrese=True
        i =0
        j =1
        while j < len(nums):
            if nums[i]>nums[j]:
                increase=False
            if nums[i]<nums[j]:
                decrese=False
            i +=1
            j +=1
        return increase or decrese

        