class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row=len(matrix)
        col=len(matrix[0])
        for __ in range(col):
            transpose_matrix=[[0 ]*row for __ in range(col)]
        
        for i in range(row):
            for j in range(col):
                transpose_matrix[j][i]=matrix[i][j]
                
        return transpose_matrix