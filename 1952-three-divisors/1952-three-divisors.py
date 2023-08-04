class Solution:
    def isThree(self, n: int) -> bool:
        new=[]
        for i in range(1,n+1):
            if n%i==0:
                new.append(i)
        return len(new)==3