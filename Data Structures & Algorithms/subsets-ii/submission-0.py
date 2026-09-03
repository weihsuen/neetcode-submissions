class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtrack(index, path):
            if index == len(nums):
                ans.append(path[:])
                return
            if index > len(nums)-1:
                return
            path.append(nums[index])

            backtrack(index+1, path)
            
            path.pop()
            while index < len(nums)-1 and nums[index] == nums[index+1]:
                index +=1
            backtrack(index+1,path)

        backtrack(0, [])
        return ans