class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg= sum(nums[: k])/k
        Sum = sum(nums[:k])
        for i in range(k, len(nums)):
            Sum += nums[i] - nums[i - k]  
            avg = max(avg,Sum / k)
        return avg
   