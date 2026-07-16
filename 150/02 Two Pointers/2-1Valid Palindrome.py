#s = "Was it a car o a cat I saw?"
#gengral sol
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for char in s:
            if char.isalnum():
                chars.append(char.lower())
        clean = "".join(chars)
        return clean == clean[::-1]
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0;right = len(s)-1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left +=1;right-=1
        return True

#print(Solution().isPalindrome(s))