nums1 = [1,3]; nums2 = [2,4]
class Solution:
    def findMedianSortedArrays(self,nums1: list[int],nums2: list[int]) -> float:
        # 確保 nums1 是比較短的陣列
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        left = 0
        right = len(nums1)  # 搜尋「取幾個」，所以不用 -1

        total_length = len(nums1) + len(nums2)
        half = (total_length + 1) // 2

        while left <= right:
            num1_choose = left + (right - left) // 2
            num2_choose = half - num1_choose

            if (
                num1_choose > 0
                and num2_choose < len(nums2)
                and nums1[num1_choose - 1] > nums2[num2_choose]
            ):
                right = num1_choose - 1

            elif (
                num2_choose > 0
                and num1_choose < len(nums1)
                and nums2[num2_choose - 1] > nums1[num1_choose]
            ):
                left = num1_choose + 1

            else:
                break

        if num1_choose == 0:
            left_max = nums2[num2_choose - 1]
        elif num2_choose == 0:
            left_max = nums1[num1_choose - 1]
        else:
            left_max = max(
                nums1[num1_choose - 1],
                nums2[num2_choose - 1]
            )

        if total_length % 2:
            return float(left_max)

        if num1_choose == len(nums1):
            right_min = nums2[num2_choose]
        elif num2_choose == len(nums2):
            right_min = nums1[num1_choose]
        else:
            right_min = min(
                nums1[num1_choose],
                nums2[num2_choose]
            )

        return (left_max + right_min) / 2
    
print(Solution().findMedianSortedArrays(nums1,nums2))