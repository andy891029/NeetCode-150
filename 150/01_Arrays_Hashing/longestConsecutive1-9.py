#nums = [2,20,4,10,3,4,5]
#nums = [0,3,5,4,6,1,1]

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        check = set(nums)
        longest = 0
        for num in check:
            if num-1 not in check:
                length = 1
                stop = num
                while stop+1 in check:
                    length +=1
                    stop += 1
                longest = max(length,longest) 
        return longest 
    
#print(Solution().longestConsecutive(nums))