class Solution:
    def bin_search(self, l, r, nums, target):
        if (len(nums) == 1 or len(nums) == 0) and nums[0] == target:
            return 0
        elif (len(nums) == 1 or len(nums) == 0) and nums[0] != target:
            return -1

        while l<=r:
            mid = l+(r-l) //2

            if nums[mid]<target:
                l = mid+1
            elif nums[mid] == target:
                return mid
            else:
                r = mid-1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        #find index of min
        while l < r:
            mid = l + (r-l) //2

            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid

        min_index = l
        #return min_index
        right_most_index = len(nums)-1

        if target == nums[min_index]:
            return min_index

        if target == nums[right_most_index]:
            return right_most_index
        
        if target < nums[right_most_index]:
            return self.bin_search(min_index, right_most_index, nums, target) 
        else:
            return self.bin_search(0, min_index, nums, target)