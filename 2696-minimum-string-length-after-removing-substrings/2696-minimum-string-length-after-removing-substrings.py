class Solution:
    def minLength(self, s: str) -> int:
        stack=[]
        stack.append(s[0])
        for i in range(1,len(s)):
            if s[i]=='B' and stack and stack[-1]=='A':
                stack.pop()
            elif s[i]=='D' and stack and stack[-1]=='C':
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack)