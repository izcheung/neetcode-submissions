from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count the number of letters for each string - hashmap
        return Counter(s) == Counter(t)