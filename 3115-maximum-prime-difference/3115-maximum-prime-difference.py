class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def isprime(n):
            if n<=1:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        prime=[]
        for i in range(len(nums)):
            if isprime(nums[i]):
                prime.append(i)
        if len(prime) < 2:
            return 0
        prime.sort()
        return prime[-1] - prime[0]
        
