class Solution:
    def finalString(self, s: str) -> str:
        string=""
        for char in range(len(s)):
            if s[char] =='i':
                string=string[::-1]
            else:
                string +=s[char]
        return string
            
        