height = [0,2,1,3,1,0,1,3,2,1] # 8

class Solution:
    def trap(self, height: list[int]) -> int:
        output = 0
        left = 0;right = len(height)-1
        left_max = 0;right_max = 0
        while left < right:
            if height[left] <= height[right]:
                left_max = max(left_max,height[left])
                output += left_max-height[left]
                left += 1
            else: 
                right_max = max(right_max,height[right])
                output += right_max-height[right]
                right -= 1
            
        return output

print(Solution().trap(height))