class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(x):
            return int(str(x)[::-1])
        count=0
        P={}
        for i in range(len(nums)):
            diff = nums[i] - rev(nums[i])
            count += P.get(diff, 0)
            P[diff] = P.get(diff, 0) + 1
        return count%(10**9 + 7)
