#nums = [-1,0,2,4,6,8]; target = 4
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0;right = len(nums)-1;mid = (right-left)//2
        while left <= right:
            if target > nums[mid]:
                left = mid + 1
                mid = left + (right-left)//2
            elif target < nums[mid]:
                right = mid - 1
                mid = left + (right-left)//2
            else:
                return mid
        return -1
#print(Solution().search(nums,target))