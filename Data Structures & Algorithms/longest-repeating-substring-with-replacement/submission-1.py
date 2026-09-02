class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # a var to keep track of how many dissimilar letter in the window
      
        # if different > k, then increment the left pointer until different <= k
        # have a variable keeping track of maxlen
        # use a hashmap to keep track of the letter (key) and the quantity of each (value)
        # ie: {q: 2}

        seen = {}
        maxLen = 0
        l = 0
        r = 0
   
        while r < len(s):
            # if s[r] not in seen:
            #     seen[s[r]] =  1
            # else:
            #     seen[s[r]] += 1

            seen[s[r]] = 1 + seen.get(s[r], 0)
            while ((r - l + 1) - max(seen.values())) > k:
                seen[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen
         


        # while r < len(s):
          
        #     if s[r] != s[l]:
        #         difference += 1
        #         if s[r] not in seen:
        #             seen[s[r]] =  1
        #         else:
        #             seen[s[r]] += 1
        #     while len(seen) > k + 1:
        #         seen.pop(s[l])
        #         l += 1
        #     maxLen = max(maxLen, r - l + 1)
        #     r += 1
         

            # if len(seen) <= k:
            #     if s[r] not in seen:
            #         seen[s[r]] = 1 # {A:3, b:1}
            #     else:
            #         seen[s[r]] += 1
            # else:
            #     while len(seen) > k:
            #         seen[s[l]] -= 1
            #         if seen[s[l]] == 0:
            #             seen.pop(s[l])
            #         l += 1
            # maxLen = max(maxLen, r - l + 1)
            # r += 1
    