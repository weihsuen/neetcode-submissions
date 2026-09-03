class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #1. Hashmap storing hashmap[num] = index
        myHash = {}
        for index, num in enumerate(nums): #O(n)
            myHash[num] = index

        for index, num in enumerate(nums):
            tofind = target - num
            if tofind in myHash and index != myHash[tofind]:
                return [index, myHash[tofind]]

        #2. Two Pointers from start

        #3. Two pointers from both ends
    

        #4. no sort, just O(n^2) double for loop
            
        