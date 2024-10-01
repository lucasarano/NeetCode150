class Solution:
    def trap(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        water = 0
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax < rightMax:
                
                l += 1
                leftMax = max(height[l], leftMax)
                water += leftMax - height[l]
            else:
                
                r -= 1
                rightMax = max(rightMax, height[r])
                water += rightMax - height[r]

        return water