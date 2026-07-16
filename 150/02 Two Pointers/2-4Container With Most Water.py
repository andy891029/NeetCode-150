#height = [1,7,2,5,4,7,3,6]
class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left = 0;right = len(heights)-1
        ans = 0
        while left < right:
            area = min(heights[left],heights[right]) * (right-left)
            if area > ans :
                ans = area
            if heights[right] >= heights[left]:
                left += 1
            else:
                right -= 1
        return ans
#print(Solution().maxArea(height))