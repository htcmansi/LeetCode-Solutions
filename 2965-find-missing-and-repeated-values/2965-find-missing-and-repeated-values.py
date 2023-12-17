class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = []
        row = len(grid)
        col = len(grid[0])
        ans = [0, 0]
        freq = {}
        for i in range(row):
            for j in range(col):
                res.append(grid[i][j])
        res.sort()
        for i in res:
            freq[i] = freq.get(i, 0) + 1
        for x in freq:
            if freq[x] == 2:
                ans[0] = x 
        for i in range(1, row * row + 1):
            if i not in res:
                ans[1] = i 
        return ans