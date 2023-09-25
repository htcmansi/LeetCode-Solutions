class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        S=sorted(s)
        T=sorted(t)
        i=0
        j=0
        while i<len(S) and j<len(T):
            if S[i]!=T[j]:
                return T[j]
            i+=1
            j+=1
        return T[-1]