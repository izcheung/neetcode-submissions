class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # longest substring length that contains only ONE char
        # I want to always target substituting the char with the least number of char
        # AABBBAA k = 3
        # Here you want to sub A first, but then after you pass the second last A, you sub B
        # i need a hashmap to keep count of how many of each char in my substring
        # Use a sliding window to keep track of my substring

        counter = {}
        left = 0
        maxLength = length = 0

        # at most two different char
        '''
        AAAAABBBBCBB k = 3
                ^
        length = 9
        maxLength = 8
        counter = {A: 5, B:4}

        '''
    
        for right in range(len(s)):
            currChar = s[right]
            length += 1

            if currChar in counter:
                counter[currChar] += 1
            else:
                counter[currChar] = 1

            # Length of the substring - the max count of the char (majority)

            while ((right - left + 1) - max(counter.values())) > k:
                leftChar = s[left]
                if counter[leftChar] == 1:
                    counter.pop(leftChar, None)
                else:
                    counter[leftChar] -= 1
                length -= 1
                left += 1

            maxLength = max(length, maxLength)
        return maxLength



        