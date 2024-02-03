class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k=j+1
                l=len(nums)-1
                while k<l:
                    if nums[i]+nums[j]+nums[k]+nums[l]==target:
                        ans.add((nums[i],nums[j],nums[k],nums[l]))
                        k +=1
                        l-=1
                    elif nums[i]+nums[j]+nums[k]+nums[l]<target:
                        k +=1
                    else:
                        l-=1
        return ans