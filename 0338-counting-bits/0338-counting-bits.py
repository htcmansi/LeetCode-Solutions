class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1) 
        count = 0 
        for i in range(1,n+1): 
            bin_n = bin(i)
            for j in str(bin_n):
                if j == "1": 
                    count += 1 
                ans[i] = count 
            count = 0
        return (ans)