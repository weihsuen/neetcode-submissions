class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = res = max(piles)


        while l<=r:
            mid = l + (r-l) //2
            hours = 0
            for item in piles:
                hours += math.ceil(item/mid)

            if hours > h:
                l = mid +1
            elif hours <= h:
                res = mid
                r = mid -1

        return res


                


