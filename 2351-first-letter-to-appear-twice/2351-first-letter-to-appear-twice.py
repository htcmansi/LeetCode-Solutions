class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letter_count = {}

        for letter in s:
            letter_count[letter] = letter_count.get(letter, 0) + 1
            if letter_count[letter] == 2:
                return letter
