class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        freq_char_pairs = []
        for char, freq in count.items():
            freq_char_pairs.append((freq, char))
        freq_char_pairs.sort(reverse=True)
        sorted_string =""
        for freq, char in freq_char_pairs:
            sorted_string += char * freq
        return sorted_string