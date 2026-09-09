from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # two pointer - right expands, left shrinks
        '''
        expand right pointer until valid, strink from left until invalid
        keep a var that marks the min string length
        keep a var that marks the start and end indices
        return the string at the end using the indices
        Use a hashmap to track the latest indicies for a letter (make sure you don't jump backwards)
        first iteration of the solution i will just compare hashmaps with hashmap O(n) but i know i can optimize it using a variable instead - wait, sMap doesn't have to be exactly equal to T, I just need to make sure it has at LEAST the letters in t, so I will use a var to keep track of the number of matches between the two hashmaps - otherwise i have to loop through the tMap everytime i want to do a comparison


        
        matches 2
        minLenght = 4
        indcies (0, 8)

        leftChar = O


        "cabwefgewcwaefgcf"
              l      r
        "cae"
        '''
        if len(s) < len(t):
            return ""


        tMap = Counter(t)
        sMap = {}
        matches = 0
        need = len(tMap)
        minLength = float('inf')
        indices = (0,0)

        '''
        matches =
        minLenght = 
        indcies (0, 0)

        "cabwefgewcwaefgcf"
              l     r
        "cae"

        char = 1
        match = 2
        need = 3
        min lenght = 5
        indices = 0,4
        '''
        l = 0
        for r in range(len(s)):
            char = s[r]
            sMap[char] = 1 + sMap.get(char, 0)

            if sMap[char] == tMap[char]:
                matches += 1
            
            # get the new shortest substring
            if matches == need and (r - l + 1) < minLength:
                minLength = (r - l + 1)
                indicies = (l, r)

            while matches == need:
                # shrink the left until it is invalid
                leftChar = s[l]
                sMap[leftChar] = sMap[leftChar] - 1
                l += 1
                if leftChar in tMap and sMap[leftChar] < tMap[leftChar]:
                    matches -= 1
                else:
                    if (r - l + 1) < minLength:
                        minLength = (r - l + 1)
                        indicies = (l, r)
           
            

        if minLength == float('inf'):
            return "" 
        else:
            return s[indicies[0]: indicies[1] + 1]
            





