class Solution:
    def removeDuplicates(self, s: str) -> str:
        i = 0
        while i+1 < len(s):
            if s[i] == s[i + 1]:
                s = s[:i] + s[i + 2:]
                if i >0:
                    i -=1
            else:
                i += 1
        return s