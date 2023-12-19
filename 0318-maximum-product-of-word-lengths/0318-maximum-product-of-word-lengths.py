class Solution:
    def maxProduct(self, words: List[str]) -> int:
        p=0
        value=0
        words=list(set(words))
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                for k in words[i]:
                    if k not in words[j]:
                        p= len(words[i])*len(words[j])
                    else:
                        p=0
                        break
                value=max(p,value)
        return value
                
