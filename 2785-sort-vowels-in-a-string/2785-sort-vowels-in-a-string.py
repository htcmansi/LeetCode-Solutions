class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        t = ['0'] * len(s)

        for i, char in enumerate(s):
            if char.lower() in 'aeiou':
                vowels.append(char)

            if char.lower() not in 'aeiou':
                t[i] = char

        vowels.sort()

        for i, char in enumerate(t):
            if char == '0':
                t[i] = vowels.pop(0)

        return ''.join(t)
        