from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = Counter(t)
        sMap = {}
        left = right = 0

        need = len(tMap)
        have = 0
        minLength = float('inf')
        minString = ""

        """
        OUZODYXAZV
        0123456
             l  r
        
        have = 3
        need = 3
        minLength = 4
        minString = YXAZ

        "XYZ"

        sMap = { U:0, Z:1, D:1, Y:1, X:1, A:1}

        """

        for right in range(len(s)):
            rightChar = s[right]
            sMap[rightChar] = 1 + sMap.get(rightChar, 0)

            if rightChar in tMap and tMap[rightChar] == sMap[rightChar]:
                have += 1
            
            while have == need:
                if right-left+1 < minLength:
                    minLength = right-left+1
                    minString = s[left:right+1]
                leftChar = s[left]
                sMap[leftChar] -= 1
          
                if leftChar in tMap and sMap[leftChar] < tMap[leftChar]:
                    have -= 1
                left += 1


        return minString






