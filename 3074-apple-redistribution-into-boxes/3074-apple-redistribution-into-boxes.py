class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort()  
        sum_apples= sum(apple)  
        res=0
        for i in range(len(capacity) - 1, -1, -1):  
            res +=1  
            sum_apples -=capacity[i]  
            if sum_apples<=0:  
                break
        return res 