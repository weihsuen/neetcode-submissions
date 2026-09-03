class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #1. myhash[ele] = freq, sort by value and print

        myhash = {}
        for num in nums:
            myhash[num] = myhash.get(num,0)+1

        sortedHash = sorted(myhash.items(), key=lambda x:x[1], reverse=True)

        sol = []
        for i in range(k):
            sol.append(sortedHash[i][0])

        return sol

        