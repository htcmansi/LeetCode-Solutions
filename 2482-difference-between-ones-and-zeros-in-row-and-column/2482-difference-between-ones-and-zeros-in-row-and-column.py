class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row=len(grid)
        col=len(grid[0])
        r=[]
        c=[]
        for i in range(row):
            c1=0
            c2=0
            for j in range(col): 
                if grid[i][j]==1:
                    c1+=1
                else:
                    c2 +=1
            r.append([c1,c2])
        for j in range(col):
            c1=0
            c2=0
            for i in range(row):
                if grid[i][j]==1:
                    c1 +=1
                else:
                    c2 +=1
            c.append([c1,c2])
        diff=[[0 ]*col for value in range(row)]
        for i in range(len(diff)):
            for j in range(len(diff[0])):
                diff[i][j]=r[i][0]+c[j][0]-r[i][1]-c[j][1]
        return diff
                