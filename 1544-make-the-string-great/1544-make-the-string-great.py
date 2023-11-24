class Solution:
    def makeGood(self, s: str) -> str:
        s1=[]
        for char in s:
            if s1 and abs(ord(char) - ord(s1[-1]))==32:
                s1.pop()
            else:
                s1.append(char)
        return "".join(s1)