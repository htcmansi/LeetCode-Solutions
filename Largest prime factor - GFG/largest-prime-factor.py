#User function Template for python3

class Solution:
    def largestPrimeFactor (self, N):
         factors = []
         divisor = 2
         while N > 1 and divisor * divisor <= N:
             if N % divisor == 0:
                 factors.append(divisor)
                 N //= divisor
             else:
                 divisor += 1

         if N > 1:
             factors.append(N)
         return max(factors)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.largestPrimeFactor(N))
# } Driver Code Ends