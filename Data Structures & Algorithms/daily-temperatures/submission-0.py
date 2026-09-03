class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #element, index

        for index, element in enumerate(temperatures):
            while stack and element > stack[-1][0]:
                thisele, thisindex = stack.pop()
                res[thisindex] = index - thisindex
            stack.append((element,index))

        return res