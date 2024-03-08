class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_freq=0
        count=0
        freq= {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for key, value in freq.items():
            max_freq = max(max_freq, value)
        for key, value in freq.items():
            if value == max_freq:
                count += max_freq
        return count