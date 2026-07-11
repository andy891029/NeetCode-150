
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        def quick(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            mid = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quick(left) + mid + quick(right)
        sort = quick(nums)
        for i in range (len(sort)-1):
            if sort[i] == sort[i+1]:
                return True
        return False