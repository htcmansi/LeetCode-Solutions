class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or=0
        prev=Counter()
        prev[0]=1
        for n in nums:
            max_or |= n
            current=Counter()
            for prev_or, cnt in prev.items():
                current[prev_or | n] += cnt
            prev.update(current)
        return prev[max_or]
        