class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        multiple=2
        while True:
            if multiple % n==0:
                return multiple
            
            multiple += 2
        
        