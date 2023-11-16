class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        arr= []
        res=""
        for i in nums:
            arr.append(int(i, 2))
        arr.sort()
        for i in range(2** len(nums)):
            if i not in arr:
                res = bin(i).replace("0b", "")
                break
        if len(res) < len(nums):
            res = '0' * (len(nums) - len(res)) + res
        return res