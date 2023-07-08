#User function Template for python3

class Solution:

    def Count(self, S):
        count=0
        alphabets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        for char in S:
            if char in alphabets:
                count +=1
                
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        print(solObj.Count(S))
# } Driver Code Ends