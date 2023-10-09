class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        """if target not in nums:
            return []
        start=0
        end=0
        for i in range(len(nums)):
            if nums[i]==target:
                start=i
                break
        for j in range(len(nums)-1,-1,-1):
            if nums[j]==target:
                end=j
                break
        return list(set([start,end]))"""
        res=[]
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(i)
        return res
        