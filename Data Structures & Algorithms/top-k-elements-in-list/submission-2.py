class Solution:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:

            #1. myhash[ele] = freq, sort by value and print
            myhash = {}
            for num in nums:
                myhash[num] = myhash.get(num,0)+1

            # sortedHash = sorted(myhash.items(), key=lambda x:x[1], reverse=True)

            # sol = []
            # for i in range(k):
            #     sol.append(sortedHash[i][0])

            # return sol

            #Bucket Sort: replace sorting hashmap with linear pass of buckets, where bucket[freq] = element

            #Put into buckets
            myBucket = [[] for _ in range(len(nums)+1)]
            for element, freq in myhash.items():
                myBucket[freq].append(element)

            #print top k
            ans = []
            for i in range(len(myBucket)-1, 0, -1):
                myarr = myBucket[i]
                for ele in myarr:
                    ans.append(ele)

                if len(ans) == k:
                    return ans





            