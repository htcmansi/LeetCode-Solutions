class Solution:
    def countDigits(self, num: int) -> int:
        num_str = str(num)
        count = 0
        for digit_str in num_str:
            digit = int(digit_str)
        
            if digit != 0 and num % digit == 0:
                count += 1
            
        return count
        