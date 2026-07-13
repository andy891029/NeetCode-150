nums = [1,1,2,2,3,3,3,5,6,6,6,7,7];k = 2
'''
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
           count[num] = count.get(num,0)+1
        ans = []
        for i in range(k):
            rank = max(count,key= count.get)
            ans.append(rank) 
            del count[rank]
        return ans
'''

from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        top_k_pairs = count.most_common(k)
        ans = []
        for item in top_k_pairs:
            ans.append(item[0]) 
        return ans
#print(Solution().topKFrequent(nums,k)) 
'''
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
           count[num] = count.get(num,0)+1

        buckets = [[] for _ in range(len(nums)+1)]
        for num,vote in count.items():
            buckets[vote].append(num)
        ans = []
        for i in range(len(nums),0,-1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans)==k:
                    return ans
        return ans
'''
#print(Solution().topKFrequent(nums,k)) 