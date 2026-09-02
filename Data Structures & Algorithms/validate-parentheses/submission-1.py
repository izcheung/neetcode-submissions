class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(":
                stack.append(")")
            elif char == "{":
                stack.append("}")
            elif char == "[":
                stack.append("]")
            else:
                if len(stack) == 0:
                    return False
                stackTop = stack.pop()
                if stackTop != char:
                    return False
        return len(stack) == 0