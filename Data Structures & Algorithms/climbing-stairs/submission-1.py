class Solution:
    def climbStairs(self, n: int) -> int:
        def recur(x):
            if x==1:
                return 1
            if x==2:
                return 2
            return recur(x-1)+recur(x-2)

        return recur(n)