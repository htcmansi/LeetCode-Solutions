class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        res = []
        ans = [[0] * c for _ in range(r)]
        if r * c != row * col:
            return mat
        for v in mat:
            for x in v:
                res.append(x)
        k = 0
        for i in range(r):
            for j in range(c):
                ans[i][j] = res[k]
                k += 1
        return ans