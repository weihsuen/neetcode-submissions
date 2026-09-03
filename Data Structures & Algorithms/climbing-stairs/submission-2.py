class Solution:
    def climbStairs(self, n: int) -> int:
        def recur(x):
            if x==n:
                return 1
            if x>=n:
                return 0
            return recur(x+1)+recur(x+2)

        return recur(0)