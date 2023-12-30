class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq =Counter()
        for word in words:
            for ch in word:
                freq[ch] += 1
        for word in words:
            for ch in word:
                if freq[ch] % len(words) != 0:
                    return False
        return True