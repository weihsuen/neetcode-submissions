class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def recur(current_number_index, cur_sum, cur_combi):
            if current_number_index >= len(nums):
                return
            if cur_sum == target:
                ans.append(cur_combi[:])
                return
            if cur_sum > target:
                return

            cur_combi.append(nums[current_number_index])
            recur(current_number_index, cur_sum+nums[current_number_index], cur_combi)
            cur_combi.pop()
            recur(current_number_index+1, cur_sum, cur_combi)

        recur(0, 0, [])
        return ans
