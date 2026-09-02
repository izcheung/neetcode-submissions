class Solution:
    def isPalindrome(self, s: str) -> bool:
     
 

        # clean the string

        # case insensitive
        # isAlnum
        # get rid of space and not letter/nums
        cleanedArray = []
        for char in s:
            if char.isalnum():
                cleanedArray.append(char.lower())
        cleanedString = "".join(cleanedArray)


       # two pointer
        i = 0
        j = len(cleanedString)-1

        while i < j:
            if cleanedString[i] != cleanedString[j]:
                return False
            i += 1
            j -= 1
        return True
