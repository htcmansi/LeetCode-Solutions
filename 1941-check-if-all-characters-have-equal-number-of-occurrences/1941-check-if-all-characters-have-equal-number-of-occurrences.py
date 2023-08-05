class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq={}
        for char in s:
            freq[char] =freq.get(char, 0) + 1
        first_freq=freq[s[0]]
        for frequency in freq.values():
            if frequency != first_freq:
                return False
        return True

                
        
        