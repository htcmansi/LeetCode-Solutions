class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        g=[(groupSizes[i],i) for i in range(len(groupSizes)) ]
        g.sort()
        i = 0
        while i < len(groupSizes):
            t = []
            j = 0
            while j < g[i][0]:
                t.append(g[i + j][1])
                j += 1
            i += j
            res.append(t)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        