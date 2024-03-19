class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_sum=int(a,2)+int(b,2)
        Binary_sum=bin(decimal_sum)
        return Binary_sum[2:]
        