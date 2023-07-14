class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        word_positions = {}

        for word in words:
            position = int(word[-1])
            word_positions[position] = word[:-1]

        sorted_words = [word_positions[i] for i in sorted(word_positions)]

        sortSentence = " ".join(sorted_words)
        return sortSentence    