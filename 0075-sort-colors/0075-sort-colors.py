class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros=nums.count(0)
        ones=nums.count(1)
        twos=nums.count(2)
        i=0
        while i < len(nums):
            while zeros!=0:
                nums[i]=0
                zeros-=1
                i+=1
            while ones!=0:
                nums[i]=1
                ones-=1
                i+=1
            while twos!=0:
                nums[i]=2
                twos-=1
                i+=1