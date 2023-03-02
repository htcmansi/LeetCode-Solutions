class Solution(object):
    def twoSum(self, nums, target):
        dec = {}
        for i, j in enumerate(nums):
            rem = target - j
            if rem in dec: return [dec[rem], i]
            dec[j] = i
        