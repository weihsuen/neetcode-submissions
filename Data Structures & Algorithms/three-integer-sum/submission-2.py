class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort it
        nums.sort()
        #myList = []
        mySet = set()

        #for each element, set then two pointers, skip if duplicated 
        for index, element in enumerate(nums):
            if index > 0 and element == nums[index-1]:
                continue
            else:
                start = index +1
                end = len(nums)-1
                while start < end: 
                    mySum = nums[start] + nums[end] + nums[index]
                    if mySum == 0:
                        #myList.append([nums[index],nums[start], nums[end]])
                        #mySet.add([nums[index],nums[start], nums[end]])
                        mySet.add((nums[index], nums[start], nums[end]))
                        start +=1
                        end -=1
                    elif mySum < 0:
                        start +=1
                    else:
                        end -=1
        return list(map(list, mySet))
                    