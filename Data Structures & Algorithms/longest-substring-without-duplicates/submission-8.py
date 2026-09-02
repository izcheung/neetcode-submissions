class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # substring = consecutive chars
        # use a set to keep track of what chars are in the window
        '''
        # just return the length
        # use a window to keep track of the longest substring
        for loop for the right pointer
        while loop inside for the left pointer (increment the left until the window is valid again (no char duplicates))


        abba
          ^^
        seen = { a:0, b: 2,  }
        length = 2
        maxLength = 1
        '''
        left = 0
        seen = {}
        maxLen = length = 0
        for i in range(0, len(s)):
            length += 1
 
            if s[i] in seen:
                consider = seen[s[i]] + 1
                left = max(consider, left)
                length = i - left + 1

            maxLen = max(maxLen, length)

            seen[s[i]] = i
        return maxLen
