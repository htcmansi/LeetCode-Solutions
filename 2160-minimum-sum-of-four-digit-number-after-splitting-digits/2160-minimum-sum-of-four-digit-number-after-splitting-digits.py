class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(list(str(num))) 
        new1 = int(''.join(digits[::2]))
        new2 = int(''.join(digits[1::2]))
        return new1 + new2
