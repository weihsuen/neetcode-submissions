class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        list_element = []

        def backtracking(decision_nums):
            nonlocal ans, list_element
            if decision_nums == len(nums):
                ans.append(list_element[:])
                return
            list_element.append(nums[decision_nums])
            backtracking(decision_nums+1)
            list_element.pop()
            backtracking(decision_nums+1)

        backtracking(0)
        return ans

            






        