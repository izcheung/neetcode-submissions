class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Use a stack
        # while it is a number, append
        stack = []

        for i, token in enumerate(tokens):
            if token == "+":
                second = stack.pop()
                first = stack.pop()
                ans = first + second
                stack.append(ans)
            elif token == "-":
                second = stack.pop()
                first = stack.pop()
                ans = first - second
                stack.append(ans)
            elif token == "*":
                second = stack.pop()
                first = stack.pop()
                ans = first * second
                stack.append(ans)
            elif token == "/":
                second = stack.pop()
                first = stack.pop()
                ans = int(first/second)
                stack.append(ans)
            else:
                stack.append(int(token))
        return stack[-1]
\
        
                
            

