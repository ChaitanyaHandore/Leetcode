class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        s = 0
        while i < j:
            a = (j - i) * min(height[i], height[j])
            s = max(s, a)
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:   # heights are equal
                j -= 1   # or i += 1, either works
        return s