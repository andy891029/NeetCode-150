
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

data = [5,34,46,1,22,21,27,64,43,22,19]
def merge(left,right):
    final = []
    i = 0;j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            final.append(left[i])
            i += 1 
        else: 
            final.append(right[j])
            j += 1
    final.extend(left[i:])
    final.extend(right[j:])
    return final
def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)
#print(merge_sort(data))

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        def merge(left,right):
            final = []
            i = 0;j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    final.append(left[i])
                    i += 1 
                else: 
                    final.append(right[j])
                    j += 1
            final.extend(left[i:])
            final.extend(right[j:])
            return final
        def merge_sort(arr):
            if len(arr) <=1:
                return arr
            mid = len(arr)//2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left,right)
        sort = merge_sort(nums)
        for i in range (len(sort)-1):
            if sort[i] == sort[i+1]:
                return True
        return False
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
#print(Solution().hasDuplicate(data))