class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        r=len(mat)
        c=len(mat[0])
        res=set()
        for i in range(r):
            count=0
            for j in range(c):
                if mat[i][j]==1:
                    count +=1
            res.add((count,i)) 
        output=[]
        s=sorted(res)
        for count,i in s:
            output.append(i)
            k-=1
            if k==0:
                break
        return output
            
            
        