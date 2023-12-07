class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1=list(s1)
        s2=list(s2)
        if s1 == s2 :
            return True
        for i in range(len(s1)):
            for j in range(1,len(s2)):
                s1[i],s1[j]=s1[j],s1[i]
                if s1 == s2:
                    return True
                s1[i], s1[j] = s1[j], s1[i]
        return False
        