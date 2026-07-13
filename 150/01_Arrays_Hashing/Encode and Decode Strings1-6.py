#strs = ["Hello,hi","World"]
strs = ["World"]
class Solution:

    def encode(self, strs: list[str]) -> str:
        encode_word = ""
        for str in strs:
            lenth = len(str)
            encode_word += f"{lenth}#{str}"
        return encode_word

    def decode(self, s: str) -> list[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            ans.append(s[j+1:j+1+length])
            i = j+1+length
        return ans

