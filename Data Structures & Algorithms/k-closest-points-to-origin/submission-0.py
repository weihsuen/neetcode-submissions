class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        myHeap = []

        for x,y in points:
            dis = (x ** 2 + y ** 2)
            heapq.heappush(myHeap, (-dis, (x,y)))
            if len(myHeap) > k:
                heapq.heappop(myHeap)

        return [point for (dis,point) in myHeap]