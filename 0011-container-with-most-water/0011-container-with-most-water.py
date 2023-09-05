class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        i = 0
        j = len(height) - 1
        while (j > i):
            l = j - i
            h = min(height[i], height[j])
            area = l * h  
            res = max(area, res)
            if height[j] > height[i]:
                i += 1;
                #res = max(l * height[j], res);
            else:
                j -= 1;
                #res = max(l * height[i], res);
        return res;