class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()  
        n = len(skill)
        total= skill[0] + skill[-1] 
        total_chemistry = 0 
        for i in range(n // 2):
            if skill[i] + skill[n - i - 1] != total:
                return -1  
            total_chemistry += skill[i] * skill[n - i - 1]
        return total_chemistry