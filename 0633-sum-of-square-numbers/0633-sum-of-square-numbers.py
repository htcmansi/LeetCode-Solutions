class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """if c<=2:
            return True  
        for i in range(c+1):
            for j in range(i+1,c+1):
                if i**2+j**2==c:
                    return True
        return False"""
        i=0
        j=int(c**0.5)
        while i<=j:
            s= i**2 +j**2
            if s == c:
                return True
            elif s < c:
                i += 1
            else:
                j -= 1  
        return False