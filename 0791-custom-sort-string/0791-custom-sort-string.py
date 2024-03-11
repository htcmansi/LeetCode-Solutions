class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res= ""
        d = {}
        for x in s:
            if x in d:
                d[x] +=1
            else:
                d[x] =1
        for char in order:
            if char in d:
                while d[char] >0:
                    res +=char
                    d[char] -=1
        for char, count in d.items():
            while count >0:
                res +=char
                count -=1
        return res