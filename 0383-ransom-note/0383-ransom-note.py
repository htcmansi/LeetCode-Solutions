class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        for char in ransomNote:
            if char not in magazine:
                return False
            else:
                 magazine.remove(char)
        return True