class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        option = []
        def dfs(openB, closeB):
            # an answer uses n open bracket and n closed bracket
            if openB == n and closeB == n:
                bracketString = "".join(option)
                ans.append(bracketString)
                return

            if openB > closeB and closeB < n:
                option.append(")")
                dfs(openB, closeB+1)
                option.pop()
            if openB < n:
                option.append("(")
                dfs(openB+1, closeB)
                option.pop()
        dfs(0,0)
        return ans