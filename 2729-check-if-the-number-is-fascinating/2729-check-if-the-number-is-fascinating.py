class Solution:
    def isFascinating(self, n: int) -> bool:
        n1=2*n
        n2=3*n
        res=str(n)+str(n1)+str(n2)
        if '0' not in res and set(res)==set('123456789') and len(res)==9:
            return True
        return False