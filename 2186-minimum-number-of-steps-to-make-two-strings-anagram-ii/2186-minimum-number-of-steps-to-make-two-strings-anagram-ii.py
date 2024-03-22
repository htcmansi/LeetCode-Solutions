class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count=Counter(s)
        t_count=Counter(t)
        count=0
        for char in s_count | t_count:
            count += abs(s_count[char]-t_count[char])
        return count