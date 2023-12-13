class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq={}
        for n in nums:
            if n in freq:
                freq[n]+=1
            else:
                freq[n]=1
        res=[]
        for n in nums:
            if freq[n]==1 and n+1 not in freq and n-1 not in freq:
                res.append(n)
        return res
    