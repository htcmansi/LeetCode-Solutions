class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                s1 = str(nums[i])
                s2 = str(nums[j])
                n1 = int(s1[0])
                n2 = int(s2[-1])
                if math.gcd(n1, n2) == 1:
                    count +=1
        return count