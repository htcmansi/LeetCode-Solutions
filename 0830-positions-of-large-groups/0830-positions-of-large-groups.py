class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        i=0
        j=0
        res=[]
        while i< len(s):
            while j < len(s) and s[i]==s[j]:
                j +=1
            if (j-i)>=3:
                res.append([i,j-1])
            i=j
        return res
        