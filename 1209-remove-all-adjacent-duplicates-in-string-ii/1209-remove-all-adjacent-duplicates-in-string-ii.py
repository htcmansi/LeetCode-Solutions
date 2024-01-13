class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack or stack[-1][0] != char:
                stack.append((char, 1))
            else:
                count = stack.pop()[1] + 1
                stack.append((char, count))
            if stack[-1][1] == k:
                stack.pop()
        res = ''
        for char, count in stack:
            res += char * count
        return res