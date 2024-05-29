class Solution:
    def numSteps(self, s: str) -> int:
        dec_num=int(s,2)
        count =0
        while dec_num !=1:
            if dec_num %2==0:
                dec_num //=2
                count +=1
            else:
                dec_num +=1
                count +=1
        return count