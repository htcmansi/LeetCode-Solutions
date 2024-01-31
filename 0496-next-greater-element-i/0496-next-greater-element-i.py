class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_element= {}
        st = []
        res=[]
        for n in reversed(nums2):
            while st and st[-1] <=n:
                st.pop()
            if not st:
                next_element[n]= -1
            else:
                next_element[n] =st[-1]
            st.append(n)
        for n in nums1:
            res.append(next_element[n])
        return res
