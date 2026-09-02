from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a set to keep track of the seen alphabet (within the sliding window)
        # Maybe i should use a queue
        queue = deque()
        if len(s) < 2:
            return len(s)
        
        l = 0
        r = 0
        maxLen = 0
        length = 0
        while r < len(s):
            while s[r] in queue:
                queue.popleft()
                length -= 1
            queue.append(s[r])
            length += 1
            r += 1
            maxLen = max(length, maxLen)
        return maxLen


            # if s[r] in seen:
            #     while s[l] != s[r]:
            #         seen.
            #         l += 1

            # if a char is in seen, then increment the left pointer
            # hmm but what if there was multiple of those letters, a set does not keep count of how many
            # xxxzx
