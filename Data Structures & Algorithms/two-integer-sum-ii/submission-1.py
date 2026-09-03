class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        mySum = 0 

        while start < end:
            mySum = numbers[start] + numbers[end]
            if mySum == target:
                return [start+1,end+1]
            elif mySum < target:
                start +=1
            else:
                end -=1


            