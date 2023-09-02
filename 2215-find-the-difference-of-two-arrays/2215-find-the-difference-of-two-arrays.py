class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        f1=[]
        f2=[]
        n1=set(nums1)
        n2=set(nums2)
        for i in n1:
            if i not in n2:
                f1.append(i)
        for i in n2:
            if i not in n1:
                f2.append(i)
        return f1,f2
        