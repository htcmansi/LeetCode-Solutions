class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        i = len(num) - 1
        while i >= 0 and num[i] == '0':
            i -= 1
        if i < 0:
            return num
        res = num[:i + 1]
        return res