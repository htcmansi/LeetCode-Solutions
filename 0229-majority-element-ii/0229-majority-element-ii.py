class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        x=len(nums)//3
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for i, j in freq.items():
            if j > x:
                res.append(i) 
        return res