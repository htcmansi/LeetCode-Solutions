class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq=25*len(arr)//100
        for i in range(len(arr)):
            if arr.count(arr[i])>freq:
                return arr[i]
        return -1
            