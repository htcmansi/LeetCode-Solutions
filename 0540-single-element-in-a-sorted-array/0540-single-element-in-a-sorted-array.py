class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        for num, freq in count.items():
            if freq == 1:
                return num