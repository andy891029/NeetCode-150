s1 = "abc"; s2 = "lecabee"

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        window_count = {};target_count = {}
        for char in s1:
            target_count[char] = target_count.get(char, 0) + 1
        for right in range(len(s2)):
            window_count[s2[right]] = window_count.get(s2[right],0)+1
            if right - left + 1 > len(s1):
                window_count[s2[left]] -= 1
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]
                left += 1
            if right - left + 1 == len(s1):
                if target_count == window_count:
                    return True
        return False

print(Solution().checkInclusion(s1,s2))