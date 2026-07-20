#s = "([{}])"
class Solution:
    
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        def decode(char) :
            if char == "]": return "["
            if char == ")": return "("
            if char == "}": return "{"
        """
        decode = {")": "(","]": "[","}": "{"}
        """
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            else :
                if len(stack) == 0:
                    return False
                if stack[-1] == decode(char):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0 #not stack
    

#print(Solution().isValid(s))
