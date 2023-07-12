#User function Template for python3

class Solution:
    def isLeap (self, N):
        if N % 4 ==0:
            if N % 100 ==0:
                if N % 400 ==0:
                    return  1
                else:
                    return 0
            else:
                return 1
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isLeap(N))
# } Driver Code Ends