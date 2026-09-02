from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # order does not matter
        # make a frequency map for string t - only when all count goes to 0 is the substring valid
        # min value will always be at least length of t
        if t == "" or len(t) > len(s):
            return ""
        hashmapT = {}

        for char in t:
            hashmapT[char] = 1 + hashmapT.get(char, 0)
        currentMap = {}
       
        l = 0
        have = 0
        need = len(hashmapT) #3
        minLength = float("inf")
        left = 0
        right = 0

        # "OUZODYXAZV", t = "XYZ"

        

        for r in range(len(s)):

            currentMap[s[r]] = 1 + currentMap.get(s[r], 0) 
            #currentMap = {O: 2, U: 1, Z: 1, D: 1, Y: 1, X: 1}
            if s[r] in hashmapT and currentMap[s[r]] == hashmapT[s[r]]:
                have += 1
            # while the window is valid
            while have == need: # 3 , 3
                if (r-l+1) < minLength: 
                    minLength = r-l+1 # 6 - 0 + 1
                    left = l # 6
                    right = r # 0
                currentMap[s[l]] -= 1
                if s[l] in hashmapT and currentMap[s[l]] < hashmapT[s[l]]:
                    have -= 1
                l += 1

        if minLength == float('inf'):
            return ""
        else:
            return s[left:right+1]



        