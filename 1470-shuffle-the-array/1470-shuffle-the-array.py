class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        start=0
        mid=len(nums)//2
        res=[]
        while start<len(nums)//2 and mid<len(nums):
            res.append(nums[start])
            start +=1
            res.append(nums[mid])
            mid +=1
        return res