class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            h1 = heapq.heappop(stones) *-1
            h2 = heapq.heappop(stones) *-1
            if abs(h1-h2):
                heapq.heappush(stones, abs(h1-h2)*-1)

        if len(stones) == 1:
            return stones[0]*-1
        if len(stones) == 0:
            return 0
