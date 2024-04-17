class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq={}
        count=0
        for n in nums:
            if n in freq:
                freq[n] +=1
            else:
                freq[n]=1
        for n1 in freq:
            if freq[n1]==1:
                count +=n1
        return count