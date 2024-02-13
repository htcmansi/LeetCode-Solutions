class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        w1=[]
        for s in words:
            if s==s[::-1]:
                w1.append(s)
        if len(w1)!=0:
            return w1[0]
        return ""