class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        for char in s:
            if char not in freq:
                freq[char] =1
            else:
                freq[char]+=1
                
        for i,char in enumerate(s):
            if freq[char]==1:
                return i
        return -1
            
        