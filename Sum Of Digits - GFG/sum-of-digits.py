#User function Template for python3

class Solution:
    def sumOfDigits (self, N):
        digit_sum=0
        num=str(N)
        
        for i in num:
            digit=int(i)
            digit_sum += digit
        return digit_sum



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.sumOfDigits(N))
# } Driver Code Ends