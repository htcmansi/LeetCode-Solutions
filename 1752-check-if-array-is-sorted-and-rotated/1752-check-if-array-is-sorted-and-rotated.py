class Solution:
    def check(self, nums: List[int]) -> bool:
        for x in range(len(nums)):
            if nums==sorted(nums):
                return True
            nums=nums[1: ]+[nums[0]]
        return False