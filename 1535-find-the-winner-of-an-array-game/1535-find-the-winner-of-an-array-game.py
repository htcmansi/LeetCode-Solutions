class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])
        if k >= len(arr):
            return max(arr)
        current_Winner = arr[0]
        count = 0
        for i in range(1, len(arr)):
            if current_Winner > arr[i]:
                count += 1
            else:
                current_Winner = arr[i]
                count = 1
            if count == k:
                return current_Winner
        return current_Winner