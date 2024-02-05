class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        min_sum=float('inf')
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]<nums[j] and nums[k]<nums[j]:
                        cur_sum=nums[i]+nums[j]+nums[k]
                        min_sum=min(cur_sum,min_sum)
        if min_sum !=float('inf'):
            return min_sum
        else:
            return -1