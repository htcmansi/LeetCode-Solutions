class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        sorted_freq = sorted(freq.values(), reverse=True)
        total = len(arr)
        removal_count = 0
        removed = 0
        for f in sorted_freq:
            removed += f
            removal_count += 1
            if removed >= total // 2:
                break
        return removal_count