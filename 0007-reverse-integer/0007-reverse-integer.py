class Solution:
    def reverse(self, x: int) -> int:
        is_negative=False
        if x<0:
            is_negative=True
            x=-x
        
        str_x=str(x)
        reverse_str=str_x[::-1]
        reverse_int=int(reverse_str)
        
        if is_negative:
            reverse_int=-reverse_int
            
        if reverse_int < -2**31 or reverse_int >2**31-1:
            return 0
        return reverse_int
        
        