from collections import deque


#nums = [1,2,1,0,4,2,6]; k = 3
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = [];q = deque()
        for right in range(len(nums)):            
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            q.append(right)
            if q[0] < right - k +1:
                q.popleft()
            if right >= k-1:
                ans.append(nums[q[0]])
        return ans


#print(Solution().maxSlidingWindow(nums,k))