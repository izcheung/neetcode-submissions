class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use a hashmap to keep track of what letters are inside the window
        # value: index
        # Use sliding window
        # Look up using hashmap is O(1)

        seen = {}
        maxLen = 0

        l = 0

        '''
        abba
          lr
        maxLen = 2
        seen = {a: 0, b:2, 

        '''
        if len(s) <= 1:
            return len(s)
        for r in range(0, len(s)):
            if s[r] in seen:
                index_to_jump = seen.get(s[r])
                l = max(index_to_jump + 1, l)
            seen[s[r]] = r
            length = r - l + 1
            maxLen = max(length, maxLen)
        return maxLen

            


