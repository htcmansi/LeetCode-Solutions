#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (self, n):
        num_str = str(n)
        num_digits = len(num_str)
        
        num = sum(int(digit) ** 3 for digit in num_str)
        
        if num == n:
            return 'Yes'
        else:
            return 'No'

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends