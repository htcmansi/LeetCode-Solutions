class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        val=0
        i=0
        j=len(nums)-1
        while i<=j:
            if i!=j:
                val += int(str(nums[i]) + str(nums[j]))
                i+=1
                j-=1
            else:
                val +=nums[i]
                i+=1
                j-=1
        return val
            
                