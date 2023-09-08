class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        Fn= []
        Fn.append([1])
        for i in range(1, numRows):
            newRow = [1]
            for j in range(i - 1):
                    newRow.append(Fn[i - 1][j] + Fn[i - 1][j + 1])
            newRow.append(1)
            Fn.append(newRow)
        return Fn






        