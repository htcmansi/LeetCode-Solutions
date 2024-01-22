class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s=s1+" "+s2
        string=s.split()
        arr=[]
        for char in string:
            if string.count(char)==1:
                arr.append(char)
        return arr