class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            if tuple(count) not in group:
                group[tuple(count)] = []
            group[tuple(count)].append(string)
        ans = []
        for value in group.values():
            ans.append(value)
        return ans
             