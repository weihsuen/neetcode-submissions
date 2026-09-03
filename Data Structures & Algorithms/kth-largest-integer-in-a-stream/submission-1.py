class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.myHeap = nums
        self.k = k
        heapq.heapify(self.myHeap)
        while len(self.myHeap) > self.k:
            heapq.heappop(self.myHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.myHeap, val)
        if len(self.myHeap) > self.k:
            heapq.heappop(self.myHeap)
        return self.myHeap[0]
        
