class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores=[]
        n=len(scores)
        for i in operations:
            if i == "+":
                Sum=scores[-2]+scores[-1]
                scores.append(Sum)
            elif i == "C":
                scores.pop()
            elif i == "D":
                scores.append(2*scores[-1])
            else:
                scores.append(int(i))
        return sum(scores)