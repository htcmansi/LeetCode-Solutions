class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans =[]
        freq =Counter(nums)
        for key, value in freq.items():
            if value == 2:
                ans.append(key)
                break
        for i in range(1, len(nums) + 1):
            if i not in freq:
                ans.append(i)
                break
        return ans