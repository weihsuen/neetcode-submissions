class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(numberofOpen, numberofClose):
            #base
            if (numberofOpen == numberofClose == n):
                res.append("".join(stack))
                return

            #option 1 "(" 
            if numberofOpen < n:
                stack.append("(")
                backtrack(numberofOpen+1, numberofClose)
                stack.pop()

            #option 2 ")"
            if numberofClose < numberofOpen:
                stack.append(")")
                backtrack(numberofOpen, numberofClose+1)
                stack.pop()

        backtrack(0,0)
        return res

        