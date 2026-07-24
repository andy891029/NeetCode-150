#piles = [1,4,3,2]; h = 9
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1;right = max(piles)
        ans = right
        while left <= right:
            mid = left + (right-left)//2
            hours = 0
            for eat_hour in piles:
                hours += (eat_hour + mid - 1)//mid
            if hours <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
#print(Solution().minEatingSpeed(piles,h))
 