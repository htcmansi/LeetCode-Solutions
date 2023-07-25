#User function Template for python3
class Solution:
	def countTriplet(self, arr, n):
	    arr.sort()
        ans = 0
        n = len(arr)
    
        for i in range(n - 1, 1, -1):
            left, right = 0, i - 1
            while left < right:
                if arr[left] + arr[right] == arr[i]:
                    ans += 1
                    left += 1
                    right -= 1
                elif arr[left] + arr[right] < arr[i]:
                    left += 1
                else:
                    right -= 1
    
        return ans
	           
	           
	    
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		arr = [int(x) for x in input().split()]

		ob = Solution()
		ans = ob.countTriplet(arr, n)
		print(ans)

# } Driver Code Ends