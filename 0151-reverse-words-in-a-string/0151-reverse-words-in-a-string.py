class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        reverse_words=words[::-1]
        reverse_string=' '.join(reverse_words)
        return reverse_string