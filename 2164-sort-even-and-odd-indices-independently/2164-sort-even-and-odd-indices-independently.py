class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        
        res = []
        i = 0
        while i < len(even) or i < len(odd):
            if i < len(even):
                res.append(even[i])
            if i < len(odd):
                res.append(odd[i])
            i += 1
        return res