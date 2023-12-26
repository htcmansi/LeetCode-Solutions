class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = {}
        l = []
        for i in pieces:
            if i[0] not in d:
                d[i[0]]= i
        for i in arr:
            if d.get(i) is not None:
                l+= d[i]
        if l==arr:
            return True
        else:
            return False

