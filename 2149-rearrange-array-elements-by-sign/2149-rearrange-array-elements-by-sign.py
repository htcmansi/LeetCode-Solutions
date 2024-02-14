class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        for num in nums:
            if num>0:
                p.append(num)
            elif num<0:
                n.append(num) 
        ans=[]
        for i in range(len(p)):
            ans.append(p[i])
            ans.append(n[i])
        return ans