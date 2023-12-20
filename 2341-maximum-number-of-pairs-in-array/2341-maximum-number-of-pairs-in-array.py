class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = 0
        ans=set()
        for n in nums:
            if n in ans:
                count += 1
                ans.remove(n)
            else:
                ans.add(n)
        return [count, len(nums) - 2 * count]
        