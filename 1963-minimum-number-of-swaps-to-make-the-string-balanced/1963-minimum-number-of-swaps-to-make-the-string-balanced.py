class Solution:
    def minSwaps(self, s: str) -> int:
        count1=0
        count2=0
        for char in s:
            if char=='[':
                count1 +=1
            else:
                count1 -=1
            if count1<0:
                count2 +=1
                count1=1
        return count2