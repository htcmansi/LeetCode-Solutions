class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        res=[0]*len(nums)
        for n in nums:
            if n %2==0:
                even.append(n)
            else:
                odd.append(n)
        i=0
        j=1
        for n in even:
            res[i]=n
            i+=2
        for n in odd:
            res[j]=n
            j+=2
        return res
                