class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=-1
        end=-1
        for i in range(len(nums)):
            if nums[i]==target:
                start =i
                break
        for j in range(len(nums)-1,-1,-1):
            if nums[j]==target:
                end =j
                break
        return [start,end]
        