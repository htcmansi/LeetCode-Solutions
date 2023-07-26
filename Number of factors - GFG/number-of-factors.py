#User function Template for python3
class Solution:
    def countFactors (self, N):
        count = 0
        i = 1
        while i * i <= N:
            if N % i == 0:
                if i * i == N:
                    count += 1
                else:
                    count += 2
            i += 1
        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.countFactors(N))
# } Driver Code Ends