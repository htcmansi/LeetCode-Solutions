class Solution:
    def toHex(self, num: int) -> str:
        if num ==0:
            return '0'
        if num <0:
            num = (2**32) + num
        
        hex_num=hex(num)
        hex_number=hex_num[2:]
        return hex_number
        
        