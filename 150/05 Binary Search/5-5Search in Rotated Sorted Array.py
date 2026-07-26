nums = [3,4,5,6,1,2]; target = 1
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0;right = len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                elif target == nums[mid]: 
                    return mid
                else:
                    left = mid + 1
            else:
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                elif target == nums[mid]: 
                    return mid
                else:
                    right = mid - 1
        return -1
print(Solution().search(nums,target))