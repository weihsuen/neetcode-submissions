from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        memo = {}

        def dfs(openN: int, closedN: int) -> List[str]:
            # If we've already computed this state, return the cached result
            if (openN, closedN) in memo:
                return memo[(openN, closedN)]

            # Base case: valid sequence found
            if openN == closedN == n:
                return [""]

            res = []

            # Option 1: Add '(' if still available
            if openN < n:
                for sub in dfs(openN + 1, closedN):
                    res.append("(" + sub)

            # Option 2: Add ')' if it does not make the sequence invalid
            if closedN < openN:
                for sub in dfs(openN, closedN + 1):
                    res.append(")" + sub)

            # Store the result before returning
            memo[(openN, closedN)] = res
            return res

        return dfs(0, 0)
