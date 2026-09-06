class Solution:
    def isValid(self, s: str) -> bool:
        # Stack
        # The resulting stack has to be empty
        # make a hashmap with the corresponding open brackets
        stack = []
        matches = {')':'(', '}':'{', ']':'['}

        '''
        []
        stack = [']']
        '''
        for char in s:
            if char in matches and len(stack) != 0:
                
                curr = stack.pop()
                if curr != matches[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
