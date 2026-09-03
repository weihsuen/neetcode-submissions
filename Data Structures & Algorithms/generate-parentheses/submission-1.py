class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def valid(s: str):
            res = 0
            for element in s:
                if element == "(":
                    res +=1
                else:
                    res -=1
                if res < 0:
                    return False
            return not res

        def dfs(s: str):
            #base
            if len(s) == 2*n:
                if valid(s):
                    res.append(s)
                return

            dfs(s + ")")
            dfs(s + "(")

        dfs("")
        return res

