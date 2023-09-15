class Solution:
    def similarPairs(self, words: List[str]) -> int:
        c=0
        for i in range(len(words)):
            for j in range(i):
                if set(words[i])==set(words[j]):
                    c +=1
        return c