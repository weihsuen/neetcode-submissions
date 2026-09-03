class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = [] #stores index,height
        stack.append((-1,0))
        maxarea = 0

        for i,h in enumerate(heights):
            while h < stack[-1][1]:
                thisindex, thisheight = stack.pop()
                maxarea = max(maxarea, (thisheight)*(i-stack[-1][0]-1))
            stack.append((i,h))

        
        # After processing all heights, calculate the area for any remaining heights in the stack
        while stack[-1][0] != -1:
            thisindex, thisheight = stack.pop()
            maxarea = max(maxarea, thisheight * (len(heights) - stack[-1][0] - 1))


        return maxarea
        
        
        