class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        v = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        s = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        for i in range(13):
            while num >= v[i]:
                roman += s[i]
                num -= v[i]
        return roman