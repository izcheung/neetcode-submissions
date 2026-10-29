class Solution:
    def numDecodings(self, s: str) -> int:

        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
                
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
       
            oneDigit = dfs(i+1)

            twoDigit = 0
            if (i+1) < len(s):
                if s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"):
                    twoDigit = dfs(i+2)

            res = oneDigit + twoDigit

            dp[i] = res
            return res


        return dfs(0)


            
            

