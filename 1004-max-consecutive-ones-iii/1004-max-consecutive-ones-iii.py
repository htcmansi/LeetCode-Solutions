class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """"count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count +=1
        return count-1""" 
        i = 0
        for j in range(len(nums)):
            k -= 1 - nums[j]
            if k < 0:
                k += 1 - nums[i]
                i += 1
        return j - i + 1