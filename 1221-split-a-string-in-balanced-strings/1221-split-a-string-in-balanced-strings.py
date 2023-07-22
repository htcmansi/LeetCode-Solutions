class Solution:
    def balancedStringSplit(self, s: str) -> int:
        max_s=0
        balance=0
        
        for char in s:
            if char == 'L':
                balance +=1
            else:
                balance -=1
                
            if balance ==0:
                max_s +=1
        return max_s
        