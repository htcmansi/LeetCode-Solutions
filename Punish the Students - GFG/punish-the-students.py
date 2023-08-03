#User function Template for python3

class Solution:
    def shouldPunish (self, roll, marks, n, avg):
        count=0
        for i in range(n):
            swapped=False
            
            for j in range(1,n-i):
                if marks[j-1]>marks[j]:
                    marks[j],marks[j-1]=marks[j-1],marks[j]
                    count =count+2
                   
   
        Sum = sum(marks)
        Sum=Sum-count
        if (Sum/n >= avg):
            return 1
        else:
            return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n, avg = input ().split ()
    n = int (n)
    avg = float (avg)
    roll = list(map(int, input().split()))
    marks = list(map(int, input().split()))
    ob=Solution()
    print (ob.shouldPunish (roll, marks, n, avg))
# } Driver Code Ends