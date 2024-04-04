class Solution:
    def maxDepth(self, s: str) -> int:
        temp = 0
        depth = 0
        for char in s:
            if char == '(':
                temp += 1
                depth = max(depth, temp)
            elif char == ')':
                temp -= 1
        return depth
        