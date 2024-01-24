class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        t1=text.split()
        count=len(t1)
        for char in t1:
            for letter in char:
                if letter in brokenLetters:
                    count -=1
                    break
        return count
                