class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        answer = 0
        for i in range(n):
            answer ^= start
            start += 2
        return answer