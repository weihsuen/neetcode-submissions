class Solution:
    def climbStairs(self, n: int) -> int:
        memoi = [-1 for _ in range(n)]
        def recur(x):
            if x <n and memoi[x] != -1:
                return memoi[x]
            if x==n:
                return 1
            if x>=n:
                return 0
            ans = recur(x+1)+recur(x+2)
            memoi[x]= ans
            return ans

        return recur(0)