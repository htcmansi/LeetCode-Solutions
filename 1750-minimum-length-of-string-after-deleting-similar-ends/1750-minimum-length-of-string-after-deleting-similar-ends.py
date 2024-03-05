class Solution:
    def minimumLength(self, s: str) -> int:
        i=0
        j=len(s) - 1
        while i < j:
            if s[i]==s[j]:
                ch=s[i]
                while i < len(s) and s[i]==ch:
                    i +=1
                while j >= 0 and s[j]==ch:
                    j -=1
            else:
                break
        if j-i + 1 < 0:
            return 0
        return j-i + 1
