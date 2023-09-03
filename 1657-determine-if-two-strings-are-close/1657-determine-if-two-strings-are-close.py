class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        w1 = Counter(word1)
        w2 = Counter(word2)
        if Counter(w1.values()) == Counter(w2.values()) and set(w1.keys()) == set(w2.keys()):
            return True
        return False