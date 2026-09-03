class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # hashmap: key as num of occurance, value as a list of nums

        count = {} 
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        bucket = [[] for _ in range(len(nums)+1)]
        for num, noOfOcc in count.items():
            bucket[noOfOcc].append(num)

        ans = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
            
        
        