class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force two pointers check --> O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False    

        # sort then two pointers? --> sorting = O(nlogn), loop = O(n) hence O(nlogn)
            # sorted_nums = sorted(nums)
            # for i in range(len(nums)-1):
            #     if (sorted_nums[i] == sorted_nums[i+1]):
            #         return True
            # return False
    
        # hashmap to keep track and return if there's a clash
        seen = set()

        for num in nums: #xn
            if num in seen: # O(1)
                return True
            seen.add(num) # O(1)
        return False