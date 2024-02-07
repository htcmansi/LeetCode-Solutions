class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n=len(s)
        c=0
        for char in s:
            if char==letter:
                c +=1
            pass
        per=c/n*100
        return int(per)