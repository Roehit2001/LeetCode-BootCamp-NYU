class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_capacity = 0
        left = 0
        right = len(height)-1
        while left < right:
            h = min(height[left],height[right])
            max_capacity = max(max_capacity, h*(right-left))
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_capacity
