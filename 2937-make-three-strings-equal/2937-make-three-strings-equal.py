class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        n=0
        n1=len(s1)
        n2=len(s2)
        n3=len(s3)
        while n< n1 and n< n2 and n<n3:
            if s1[n] == s2[n] and s2[n] == s3[n]:
                n += 1
            else:
                break
        if n== 0:
            return -1
        return (n1 + n2 + n3 - (n*3))