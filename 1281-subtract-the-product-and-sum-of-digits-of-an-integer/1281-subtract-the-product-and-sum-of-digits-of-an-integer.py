class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Sum=0
        prod=1
        n=str(n)
        for i in n:
            Sum +=int(i)
            prod *=int(i)
        return prod-Sum