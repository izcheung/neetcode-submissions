class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for string in strs:
            sortedWord = "".join(sorted(string))
            if sortedWord not in words:
                words[sortedWord] = [string]
            else:
                words[sortedWord].append(string)
        return list(words.values())
        