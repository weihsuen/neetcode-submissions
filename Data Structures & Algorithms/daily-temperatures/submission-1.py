class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        n = len(temperatures)

        for i in range(n-2, -1, -1):
            j = i+1
            nil = 0
            while j<n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    nil =1
                    break
                j += res[j]

            if nil == 0:
                res[i] = j - i

        return res

