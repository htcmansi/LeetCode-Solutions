#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr, n):
        freq={}
        for num in arr:
            freq[num]=freq.get(num,0)+1
            
        for num in arr:
            if freq[num]==1:
                return num
            
        return None
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict 

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
    
# } Driver Code Ends