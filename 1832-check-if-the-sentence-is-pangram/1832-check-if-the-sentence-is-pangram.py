class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = set("abcdefghijklmnopqrstuvwxyz")
        if set(sentence) == alphabets:
            return True
        else:
            return False