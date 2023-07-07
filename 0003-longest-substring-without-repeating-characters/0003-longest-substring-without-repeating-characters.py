class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = {}
        max_length = 0
        start = 0

        for end in range(n):
            if s[end] in seen:
                start = max(start, seen[s[end]] + 1)
            seen[s[end]] = end  
            max_length = max(max_length, end - start + 1)

        return max_length
        