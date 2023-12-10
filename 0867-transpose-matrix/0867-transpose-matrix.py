class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r=len(matrix)
        c=len(matrix[0])
        for value in range(c):
            t=[[0 ]*r for value in range(c)]
        for i in range(r):
            for j in range(c):
                t[j][i]=matrix[i][j]      
        return t