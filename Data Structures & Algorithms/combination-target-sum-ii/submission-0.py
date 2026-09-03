class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def recur(index, path, cursum):
            if cursum == target:
                ans.append(path[:])
                return
            if index >= len(candidates):
                return
            if cursum > target:
                return

            
            path.append(candidates[index])
            recur(index+1, path, cursum+candidates[index])
            path.pop()
            while (index < len(candidates)-1 and candidates[index] == candidates[index+1]):
                index+=1
            recur(index+1, path, cursum)

        recur(0, [], 0)
        return ans

            