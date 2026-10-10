class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        curr_water = 0
        max_water = 0

        while left < right:
            w = right - left
            ht = min(height[left], height[right])
            curr_water = w * ht
            max_water = max(max_water, curr_water)

            if height[left] < height[right]:
                left += 1
            else:
                right -=1

        return max_water