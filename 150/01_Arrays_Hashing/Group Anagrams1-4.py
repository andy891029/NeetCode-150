#strs = ["act","pots","tops","cat","stop","hat"]
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        def sort(str: str)->str:
            result = {}
            for char in str:
                result[char] = result.get(char,0)+1
            back = []
            for i in range(26):
                number = chr(ord('a')+i)
                if number in result:
                    back.append(number*result[number])
            return back
        all_map = {}
        for s in strs:
            sorted_s = "".join(sort(s))
            if sorted_s not in all_map:
                all_map[sorted_s] = []
            all_map[sorted_s].append(s)
        return list(all_map.values())
#print(Solution().groupAnagrams(strs))