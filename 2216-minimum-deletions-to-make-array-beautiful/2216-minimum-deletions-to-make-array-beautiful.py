class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        count=0
        c1=0
        for i in range(len(nums) - 1):
            if nums[i] ==nums[i + 1] and c1 % 2 ==0:
                count += 1
            else:
                c1 += 1
        if c1 % 2 ==0:
            count += 1
        return count
