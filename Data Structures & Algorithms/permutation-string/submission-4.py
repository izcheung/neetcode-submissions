from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        mapOne = Counter(s1)
        mapTwo = {}

        '''
        s1 = "abc", 

        lecabee
         l r 
        
        mapOne = {a: 1, b:1, c:1}
        mapTwo = {e:1, c:1, a:1}

        '''

        l = 0
        for r in range(len(s2)):
            rightChar = s2[r]
            mapTwo[rightChar] = 1 + mapTwo.get(rightChar, 0)

            window_size = r - l + 1

    
            if window_size > len(s1):
                mapTwo[s2[l]] -= 1
                if mapTwo[s2[l]] == 0:
                    mapTwo.pop(s2[l])
                l += 1
            if mapOne == mapTwo:
                return True
        return False
            

            



