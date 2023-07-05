#User function Template for python3

def reverseWord(s):
    characters = s.split()
    rev_characters=[char[::-1] for char in characters]
    reverseWord=" ".join(rev_characters)
        
    return reverseWord


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends