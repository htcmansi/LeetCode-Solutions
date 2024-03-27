class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)  
        score=0
        count=0
        while count<k:
            max_element=nums[0]  
            if max_element == 0:  
                break
            score +=max_element  
            nums[0] +=1  
            count +=1 
        return score
       
            