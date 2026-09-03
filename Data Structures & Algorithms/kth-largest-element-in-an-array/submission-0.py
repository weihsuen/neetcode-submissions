class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #minheap

        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)

        return heapq.heappop(nums)