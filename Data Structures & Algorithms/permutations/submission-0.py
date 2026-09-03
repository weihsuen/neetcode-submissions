class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [0] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if used[i] == 0:
                    used[i] = 1 
                    path.append(nums[i])
                    backtrack(path)
                    used[i] = 0
                    path.pop()

        backtrack([])
        return ans

        