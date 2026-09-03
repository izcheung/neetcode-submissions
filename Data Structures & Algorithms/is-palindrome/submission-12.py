class Solution:
    def isPalindrome(self, s: str) -> bool:


        formattedString = [char.lower() for char in s if char.isalnum()]
        i = 0
        j = len(formattedString)-1
        while i < j:
            if formattedString[i] != formattedString[j]:
                return False
            i += 1
            j -= 1
        return True