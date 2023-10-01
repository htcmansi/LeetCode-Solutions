class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        rev_words = [word[::-1] for word in words]  
        rev_sentence = " ".join(rev_words)  
        
        return rev_sentence