class Solution:
    def bin_search(self, l: int, r:int, nums: List[int], target: int):
        mid = l+(r-l) //2

        if l>r:
            return -1

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            return self.bin_search(mid +1, r, nums, target)
        

        return self.bin_search(l, mid-1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.bin_search(0, len(nums)-1, nums, target)


        