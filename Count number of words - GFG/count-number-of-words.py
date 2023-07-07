#User function Template for python
class Solution:

    def countWords(self, s):
        if ("\\n" not in s and "\\t" not in s):
            return len(s.split())
        elif ("\\n" in s and "\\t" not in s):
            s = s.replace("\\n", " ")
            return len(s.split())
        elif ("\\t" in s and "\\n" not in s):
            s = s.replace("\\t", " ")
            return len(s.split())
        else:
            s = s.replace("\\n", " ")
            s = s.replace("\\t", " ")
            return len(s.split())


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.countWords(s))
# } Driver Code Ends