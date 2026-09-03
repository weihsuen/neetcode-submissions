class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #two pointers
        left = 0 
        right = 1
        curmax = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                curmax = max(curmax, prices[right]-prices[left])
            right +=1

        return curmax
        