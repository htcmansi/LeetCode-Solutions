class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = [0] * 101  
        for num in nums:
            counts[num] += 1

        for i in range(1, 101):
            counts[i] += counts[i - 1]

    
        result = [counts[num - 1] if num > 0 else 0 for num in nums]

        return result
        