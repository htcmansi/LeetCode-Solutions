class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans=""        
        while columnNumber>0:
            result=chr(ord('A')+(columnNumber-1)%26)
            ans=result+ans
            columnNumber=(columnNumber-1)//26            
        return ans
        