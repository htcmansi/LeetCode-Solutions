class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        for n in nums:
            if n in freq:
                freq[n] +=1
            else:
                freq[n]=1
        
        for num,n in freq.items():
            if n==1:
                return num
        