class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # substring = consecutive chars
        # use a set to keep track of what chars are in the window
        '''
        # just return the length
        # use a window to keep track of the longest substring
        for loop for the right pointer
        while loop inside for the left pointer (increment the left until the window is valid again (no char duplicates))

        zxyzxyz
          ^ ^
        seen = {z,x,y,}
        length = 4
        maxLength = 3
        '''
        left = 0
        seen = set()
        maxLen = length = 0
        for i in range(0, len(s)):
            length += 1
 
            while s[i] in seen:
                seen.remove(s[left])
                length -= 1
                left += 1

            maxLen = max(maxLen, length)

            seen.add(s[i])
        return maxLen
