class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans=[0] * 60
        count= 0
        for t in time:
            rem= t % 60
            complement= (60 - rem) % 60
            count += ans[complement]
            ans[rem] += 1
        return count