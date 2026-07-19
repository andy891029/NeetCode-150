#s = "OUZODYXAZV"; t = "XYZ"
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        window_count = {};target_count = {}
        for char in t:
            target_count[char] = target_count.get(char, 0) + 1
        need = len(target_count)
        need_have = 0 #滿足幾個
        min_length = float("inf")
        result = 0
        for right in range(len(s)):
            window_count[s[right]] = window_count.get(s[right],0)+1
            if s[right] in target_count and window_count[s[right]] == target_count[s[right]]:
                need_have += 1
            
            while need == need_have:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = left
                if s[left] in target_count and window_count[s[left]] == target_count[s[left]]:
                    need_have -= 1
                window_count[s[left]] -= 1
                left += 1
        if min_length == float("inf"):
            return ""
        return s[result : result + min_length]
#print(Solution().minWindow(s,t))