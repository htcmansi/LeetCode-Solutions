class Solution:
    def findComplement(self, num: int) -> int:
        bin_num=bin(num)[2:]
        complement=''
        for n in bin_num:
            complement += '1' if n == '0' else '0'
        complement_int=int(complement,2)
        return complement_int