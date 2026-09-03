class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #convert all values to a set 
        mySet = set(nums)
        overallMax = 0


        #cFor each element, check if it has a left neighbour
        for num in mySet:
            if num-1 not in mySet:
                curMax = 1
                while num+1 in mySet:
                    curMax +=1
                    num +=1 
                overallMax = max(overallMax, curMax)

        return overallMax
                    

        #if it does, conitnue
        # else,cycle until entire sequence is found 
        #update max value and return 


        