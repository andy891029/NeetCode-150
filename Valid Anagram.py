#s="racecar" ;t="carrace"
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_sort = sorted(s)
        t_sort = sorted(t)
        if s_sort == t_sort:
            return True
        return False


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            count[char] = count.get(char,0)+1
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        return True
#print(Solution().isAnagram(s,t))