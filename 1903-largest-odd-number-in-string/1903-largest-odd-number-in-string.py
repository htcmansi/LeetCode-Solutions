class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans=""
        curr=""
        for n in num:
            curr +=n
            if int(n)%2!=0:
                ans = max(ans, curr)
        return ans

        
        """if int(num)%2 !=0:
            ans=num
        else:
            for n in num:
                if int(n)%2!=0:
                    ans +=n 
        return ans"""
            
            