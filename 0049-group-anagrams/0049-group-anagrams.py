class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            
            if sorted_s in ans:
                ans[sorted_s].append(s)
            else:
                ans[sorted_s] = [s]
        return list(ans.values())