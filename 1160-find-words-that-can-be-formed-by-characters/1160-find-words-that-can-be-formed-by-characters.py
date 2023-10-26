class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for word in words:
            freq = {}
            formed = True
            for c in chars:
                if c in freq:
                    freq[c] += 1
                else:
                    freq[c] = 1

            for c in word:
                if c not in chars:
                    formed = False
                    break
                freq[c] -= 1
                if freq[c] < 0:
                    formed = False
                    break
            if formed:
                res += len(word)
        return res