class Solution:
    def minimumSteps(self, s: str) -> int:
        zero_count=0
        res=0
        for char in range(len(s)-1,-1,-1) : 
            if s[char]=='0':
                zero_count +=1
            else:
                res +=zero_count
        return res
        