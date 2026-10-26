class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestLen = 0
        longestPal = ''
        for i in range(len(s)):
            # Odd len palidrome
            l,r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > longestLen:
                    longestLen = r-l+1
                    longestPal = s[l:r+1]
                l -= 1
                r += 1
            # even length
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > longestLen:
                    longestLen = r-l+1
                    longestPal = s[l:r+1]
                l -= 1
                r += 1 
            
        return longestPal

