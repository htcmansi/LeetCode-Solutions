class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        count = 0
        ans = []
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                count += 1
            else:
                ans.append(count + 1)
                count = 0
        ans.append(count + 1)
        ans.sort()
        for i in ans:
            print(i, end=' ')
        return ans[-1]