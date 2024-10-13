class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = []
        for num in nums:
            if freq[num] > 0:
                if freq[num] > 2:
                    freq[num] = 2 
                ans.append(num)
                freq[num] -= 1
        nums[:len(ans)] = ans  
        return len(ans)
