class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        C = 0  
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i] == [grid[k][j] for k in range(len(grid))]:
                    C += 1
        return C

        