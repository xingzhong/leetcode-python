class Solution:
    # @return an integer
    def maxArea(self, height):
        area = 0
        left, right = 0, len(height)-1
        while left < right :
            area = max(area, (right-left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return area
