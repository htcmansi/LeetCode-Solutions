class Solution:
    def maxScore(self, s: str) -> int:
        mid=len(s)//2
        max_score=0
        for mid in range(len(s)):
            left=s[:mid]
            right=s[mid:]
            if len(left)!=0 and len(right)!=0:
                l1=left.count('0')
                R1=right.count('1')
                score=(l1+R1)
                max_score=max(max_score,score)
        return max_score