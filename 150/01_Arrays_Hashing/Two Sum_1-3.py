#nums = [4,5,6]; target = 10
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
#print(Solution().twoSum(nums,target))
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            another = target - num
            if another in seen:
                return [seen[another],i]
            seen[num] = i
