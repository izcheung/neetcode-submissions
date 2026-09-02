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

        return cleanedString == cleanedString[::-1]