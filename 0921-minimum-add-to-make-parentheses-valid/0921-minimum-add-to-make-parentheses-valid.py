class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count=0
        count2=0
        for char in s:
            if char=='(':
                count +=1
            elif char==')':
                if count>0:
                    count -=1
                else:
                    count2 +=1  
        return count+count2
                