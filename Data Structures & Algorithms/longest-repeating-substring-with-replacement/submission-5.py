class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # substring - think sliding window
        # you always try to substitute the letters with the least number of occurance
        # The number of letters you need to sub is the
        #  window size - (number of majority letter)
        '''
        When do you update the left pointer? when the k (we will decrement it, reaches negative)
        Use a hashmap to keep count of frequency
        Use a var to know the count of the most frequent letter

        AAABABB
        l r
        currentChar = X
        l = 0
        mostFreqLetterCount = 2
        seen = {X: 1, Y:2
        length = 
        3 - 2 = 1
        maxLen = 2

        1-1 =0 
        '''
        l = 0
        maxLen = 0
        mostFreqLetterCount = 0
        seen = {}

        for r in range(len(s)):
            currentChar = s[r]
            if currentChar not in seen:
                seen[currentChar] = 0
            seen[currentChar] += 1

            mostFreqLetterCount = max(mostFreqLetterCount, seen[currentChar])
            
            while (r - l + 1) - mostFreqLetterCount > k:
                leftChar = s[l]
                seen[leftChar] -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)
        return maxLen


