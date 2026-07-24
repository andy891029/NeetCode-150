#matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]; target = 10
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left = 0;right = len(matrix)-1
        while left <= right:
            mid = left + (right-left)//2
            if target > matrix[mid][-1]:
                left = mid + 1
            else:
                right = mid - 1
        row = left
        if row == len(matrix): return False
        left_row = 0;right_row = len(matrix[0])-1
        while left_row <= right_row:
            mid = left_row + (right_row-left_row)//2
            if target > matrix[row][mid]:
                left_row = mid + 1
            elif target < matrix[row][mid]:
                right_row = mid - 1
            else:
                return True
        return False
#print(Solution().searchMatrix(matrix,target))