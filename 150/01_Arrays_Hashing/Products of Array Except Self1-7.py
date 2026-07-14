nums = [1,2,4,6]
#nums = [-1,0,1,2,3]
'''
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = []
        i = 0
        while i < len(nums):
            sol = 1
            times = nums[:i]+nums[i+1:]
            for j in range(len(nums)-1):
                sol *= times[j]
            ans.append(sol)
            i +=1
        return ans
'''
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = []
        sol = 1
        
        for i in range(len(nums)):
            ans.append(sol)
            sol *= nums[i]
        sol = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= sol
            sol *= nums[i]

        return ans        
        
print(Solution().productExceptSelf(nums))
