class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost=sorted(cost,reverse=True)
        res=0
        count=1
        for i in range(len(cost)):
            if count ==3:
                count =1
                continue
            res +=cost[i]
            count +=1
        return res
        