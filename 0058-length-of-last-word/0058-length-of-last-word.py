class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=s.split()
        if len(words)>0:
            last_word=words[-1]
            length=len(last_word)
            return length
        else:
            return 0
        