class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        """maxWidth=0
        for i in range(len(nums)):
            for j in range(len(nums)-1,i,-1):
                if nums[i]<=nums[j]:
                    maxWidth=max(maxWidth,j-i)
                    break
        return maxWidth"""
        n = len(nums)
        sorted_indices = sorted(range(n), key=lambda x: nums[x])
        maxWidth = 0
        minIndex = n
        for idx in sorted_indices:
            maxWidth = max(maxWidth, idx - minIndex)
            minIndex = min(minIndex, idx)
        return maxWidth