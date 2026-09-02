class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use strings (because they are immutable and can be keys of a hashmap)
        # sort each string - if they are in the hashmpa, then append it to the hashmap (the original form), at the end, loop through the entire hashmap and just form the list
        seen = {}
        for word in strs:
            sortedStr = "".join(sorted(word))
            if sortedStr not in seen:
                seen[sortedStr] = []
            seen[sortedStr].append(word)
        result = []
        for value in seen.values():
            result.append(value)
        return result


