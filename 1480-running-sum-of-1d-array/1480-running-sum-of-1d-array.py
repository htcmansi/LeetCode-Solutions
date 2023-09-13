class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total=0
        result=[]
        for i in range(len(nums)):
            total=sum(nums[:i+1])
            result.append(total)
        return result
            