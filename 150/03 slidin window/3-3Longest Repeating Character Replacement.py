#s = "XYXY"; k = 2
#s = "AAABABB"; k = 1
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0;longest = 0;max_frequency = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_frequency = max(max_frequency,count[s[right]])
            window_length = right - left + 1
            need_change = window_length - max_frequency
            if need_change > k:
                count[s[left]] -= 1
                left += 1
            longest = max(longest,right - left + 1)
             
        return longest
#print(Solution().characterReplacement(s,k))