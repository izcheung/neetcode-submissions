class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Each index represents the frequency of the char
        # Turn it into a tuple and make it the key - all anagrams will have the same tuple
        # All lower case so 26
        seen = {}
        for word in strs:
            count = [0] * 26
            for i in range(len(word)):
                charOrd = ord(word[i]) - ord('a')
                count[charOrd] += 1
            count = tuple(count)
            if count not in seen:
                seen[count] = []
            seen[count].append(word)
        return [word for word in seen.values()]

