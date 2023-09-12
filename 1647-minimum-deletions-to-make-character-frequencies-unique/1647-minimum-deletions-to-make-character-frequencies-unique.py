class Solution:
    def minDeletions(self, s: str) -> int:
        f={}
        freq=set()
        d=0
        for i in s:
            if i in f:
                f[i] +=1
            else:
                f[i]=1 
        for key,value in f.items():
            while value in freq:
                value -=1
                d +=1
            if value >0:
                freq.add(value)
        return d
        