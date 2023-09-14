class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        output=[]
        for n in nums:
            str_n=str(n)
            for i in str_n:
                int_i=int(i)
                output.append(int_i)
        return output
    
      