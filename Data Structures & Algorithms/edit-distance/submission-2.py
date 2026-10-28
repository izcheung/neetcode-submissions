class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # THink coin change 
        # Three choices unlimited times
        memo = {}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            
            # Add the rest of the char in word1
            if i == len(word1):
                return len(word2) - j
            # Delete the rest of the char in word1
            if j == len(word2):
                return len(word1) - i

            if word1[i] != word2[j]:
                minOp = float('inf')
                insert = 1 + dfs(i, j+1)
                delete = 1 + dfs(i+1, j)
                replace = 1 + dfs(i+1, j+1)

                minOp = min(replace,insert,delete)
                memo[(i,j)] = minOp
                return minOp
            else:
                res = dfs(i+1, j+1)
                memo[(i,j)] = res
                return res
                

        return dfs(0,0)
