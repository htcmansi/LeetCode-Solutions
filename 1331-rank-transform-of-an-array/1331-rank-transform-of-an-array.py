class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num=sorted(arr)
        rank=1
        freq={}
        for n in num:
            if n not in freq:
                freq[n]=rank
                rank +=1
        res=[]
        for n in arr:
            res.append(freq[n])
        return res