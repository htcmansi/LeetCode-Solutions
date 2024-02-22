class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        i = 0
        j = len(nums) - 1
        while i <= j:
            ans.append(nums[i])
            if i == j:
                break
            ans.append(nums[j])
            i += 1
            j -= 1
        return ans