class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        sorted_s=sorted(s,reverse=True)
        sorted_s.append(sorted_s.pop(0))
        return ''.join(sorted_s)
