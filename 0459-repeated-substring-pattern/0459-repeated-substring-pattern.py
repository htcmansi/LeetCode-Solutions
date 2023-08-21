class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        string=(s+s)[1:-1]
        if s in string:
            return True
        return False
        