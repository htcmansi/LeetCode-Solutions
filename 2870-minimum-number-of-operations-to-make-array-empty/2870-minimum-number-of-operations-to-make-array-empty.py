class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=Counter(nums)
        count=0
        for i in c.values():
            if i==1:
                return -1
            count +=i//3
            if i%3:
                count +=1
        return count
         
        
        """count=0
        i=0
        while i<len(nums):
            j=i+1
            while j<len(nums) and nums[i]==nums[j]:
                nums.pop(j)
                count +=1
            i=j
            if i<len(nums):
                k=i+1
                while k<len(nums) and j<len(nums) and nums[i]==nums[j]==nums[k]:
                    nums.pop(i)
                    nums.pop(j)
                    nums.pop(k)
                    count +=1
                    j=i+1
                    k=j+1
                i=k          
        if len(nums)==0:
            return count
        return -1"""
        