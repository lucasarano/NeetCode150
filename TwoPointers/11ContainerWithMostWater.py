class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            area = max(area, ((j - i) * min(height[i], height[j])))
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return area
        