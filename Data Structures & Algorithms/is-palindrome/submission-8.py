class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s)-1
        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and i < j:
                j -= 1
            # i and j has to be a num or alpha
            if s[i].lower() != s[j].lower():
                return False
        
            i += 1
            j -= 1
        return True



        # cleaned = [char.lower() for char in s if char.isalnum()]
        # i = 0
        # j = len(cleaned)-1
        # while i < j:
        #     if cleaned[i] != cleaned[j]:
        #         return False
        #     i += 1
        #     j -= 1
        # return True
        # or
        # return cleaned == cleaned[::-1]