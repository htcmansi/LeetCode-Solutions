#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
	    current=arr[0]
	    prev=0
	    
	    for i in range(1,n):
	        new_current=arr[i]+prev
	        new_prev=max(current,prev)
	        
	        current=new_current
	        prev=new_prev
	                
	  
	
	    return max(current,prev)

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends