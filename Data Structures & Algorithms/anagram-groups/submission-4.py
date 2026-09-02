class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Group anagrams together using a hashmap
        # The key will be the sorted string of the anagram (all of the anagram strings iwll be the same)
        # Iterate through the hashmap values and append that into the result array
        anagrams = {}
        for word in strs:
            sortedString = str(sorted(word))
            if sortedString not in anagrams:
                anagrams[sortedString] = []
            anagrams[sortedString].append(word)
        return [value for value in anagrams.values()]
        