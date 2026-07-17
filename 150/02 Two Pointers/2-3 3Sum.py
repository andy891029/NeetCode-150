#nums = [-1,0,1,2,-1,-4]
#nums = [-2, 0, 0, 2, 2] #-2 0 0 2 2 
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        i = 0
        ans = []
        while i < len(nums)-2:
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                fin_sum = nums[i] + nums[left] + nums[right]
                if fin_sum < 0:
                    left += 1
                elif fin_sum > 0:
                    right -= 1
                else:
                    ans.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            i+=1
        return ans
#print(Solution().threeSum(nums))