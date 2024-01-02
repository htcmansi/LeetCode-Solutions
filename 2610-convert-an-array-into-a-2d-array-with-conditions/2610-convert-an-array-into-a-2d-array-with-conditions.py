class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count=Counter(nums)
        arr=[]
        for x,v in count.items():
            for i in range(v):
                if len(arr)<=i:
                    arr.append([])
                arr[i].append(x)
        return arr