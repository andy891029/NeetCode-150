#numbers = [1,2,3,4]; target = 3
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            if numbers[left]+numbers[right] < target:
                left += 1
            if numbers[left]+numbers[right] > target:
                right -= 1
            if numbers[left]+numbers[right] == target:
                return [left+1,right+1]
#print(Solution().twoSum(numbers,target))