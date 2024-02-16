class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        dist_int = set(nums)
        for num in nums:
            reversed_num = int(str(num)[::-1])
            dist_int.add(reversed_num)
        return len(dist_int)