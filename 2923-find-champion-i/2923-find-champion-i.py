class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        ans = []
        cnt = -1
        champ = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if i != j and grid[i][j] == 1:
                    ans.append(i)
                else:
                    ans.append(j)
        freq = defaultdict(int)
        for i in ans:
            freq[i] += 1
            if freq[i] > cnt:
                champ = i
                cnt = freq[i]
        return champ