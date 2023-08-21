class Solution:
    def secondHighest(self, s: str) -> int:
        num=[]
        for char in s:
            if char.isdigit():
                num.append(int(char))
        num=sorted(set(num),reverse=True)
        if len(num)>1:
            return num[1]
        else:
            return -1
        