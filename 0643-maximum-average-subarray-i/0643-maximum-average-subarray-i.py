class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = float('-inf')
        Sum = 0
        i= 0
        j= 0
        while j < len(nums):
            Sum += nums[j]
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                temp = Sum / k
                avg = max(avg, temp)
                Sum -= nums[i]
                i += 1
                j += 1
        return avg