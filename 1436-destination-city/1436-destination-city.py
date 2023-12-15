class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s=set()
        d=set()
        for p in paths:
            s.add(p[0])
            d.add(p[1])
        for d1 in d:
            if d1 not in s:
                return d1
            
        