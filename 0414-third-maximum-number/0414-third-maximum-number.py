class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num = []
        for i in nums:
            if i not in num:
                num.append(i)
        num.sort()
        if len(num) <=2:
            return max(num)
        elif len(num) >=3:
            return num[-3]
    
            
        