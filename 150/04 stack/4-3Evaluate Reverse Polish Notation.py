#tokens = ["1","2","+","3","*","4","-"]
'''
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {"+","-","*","/"}
        for char in tokens:
            if char not in operators:
                stack.append(int(char))
            else:
                ans = int(eval(f"{stack[-2]}{char}{stack[-1]}"))
                del stack[-1]
                stack[-1] = ans
        return stack[-1]
'''        
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {"+","-","*","/"}
        for char in tokens:
            if char not in operators:
                stack.append(int(char))
            else:
                right = stack.pop();left = stack.pop()
                if char == "+":
                    ans = left + right
                elif char == "-":
                    ans = left - right
                elif char == "*":
                    ans = left * right
                else:
                    ans = int(left/right)
                stack.append(ans)

        return stack[-1]
#print(Solution().evalRPN(tokens))