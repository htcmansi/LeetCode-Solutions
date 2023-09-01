class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a=0
        h=a
        for i in gain:
            a+=i
            h=max(h,a)
        return h