class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        c = Counter()
        res = [[], []]
        for match in matches:
            c[match[1]] += 1
        for key, value in c.items():
            if value == 1:
                res[1].append(key)
        for match in matches:
            if c[match[0]] == 0:
                res[0].append(match[0])
            c[match[0]] = 1
        res[0].sort()
        res[1].sort()
        return res