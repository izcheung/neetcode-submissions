class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = [char.lower() for char in s if char.isalnum()]
        # i = 0
        # j = len(cleaned)-1
        return cleaned == cleaned[::-1]
        # while i < j:
        #     if cleaned[i] != cleaned[j]:
        #         return False
        #     i += 1
        #     j -= 1
        # return True