class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}
        for letter in s:
            if letter in dictS:
                dictS[letter] += 1
            else:
                dictS[letter] = 1
        for letter in t:
            if letter in dictT:
                dictT[letter] += 1
            else:
                dictT[letter] = 1
        return dictS == dictT
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # make two dictionaries, with the letter as the key, and the number of occurences as the value
        # check if the two dictionaries are the same
        # if they are, true, if not return false
        # how to compare dictionaries - objects

        # After:
        # I can compare the length of the two strings first

        # def makeDictionary(string):
        #     dictionary = {}
        #     for letter in string:
        #         if letter in dictionary:
        #             dictionary[letter] += 1
        #         else:
        #             dictionary[letter] = 1
        #     return dictionary
        
        # firstDictionary = makeDictionary(s)
        # secondDictionary = makeDictionary(t)
        # if firstDictionary == secondDictionary:
        #     return True
        # return False

        