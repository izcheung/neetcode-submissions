class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(s):
                return True

            for word in wordDict:
                length = len(word)
                substring = s[i:i+length]
                if substring == word:
                    if dfs(i+length):
                        return True
            memo[i] = False
            return False
        return dfs(0)
