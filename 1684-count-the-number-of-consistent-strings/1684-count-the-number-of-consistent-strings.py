class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for i in range(len(words)):
            is_consistant=True
            for j in range(len(words[i])):
                if words[i][j] not in allowed:
                    is_consistant=False
            if is_consistant==True:
                count +=1
        return count