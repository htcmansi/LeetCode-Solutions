class Solution:
    def largestGoodInteger(self, num: str) -> str:
        s=""
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                s1=num[i:i+3]
                if s1>s:
                    s=s1
        return s
                    
                    
                    
                    
            