class Solution:
    def countAsterisks(self, s: str) -> int:
        barcount = 0
        count=0 
        for i in s : 
            if i =="|":
                barcount+=1
            if barcount==2:
                barcount = 0 
            if barcount==0 and i =="*":
                count+=1
        return(count)