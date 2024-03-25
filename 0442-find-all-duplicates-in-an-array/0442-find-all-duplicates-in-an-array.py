class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        frequency={}
        duplicates=[]
        for num in nums:
            if num in frequency:
                frequency[num] +=1
            else:
                frequency[num] =1
        for num, count in frequency.items():
            if count>1:
                duplicates.append(num)
        return duplicates