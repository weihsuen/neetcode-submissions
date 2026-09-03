class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0

        for index, height in enumerate(heights):
            if stack and height > stack[-1][1]:
                stack.append((index, height))
            else:
                while stack and height < stack[-1][1]:
                    indexpop, heightpop = stack.pop()
                    width = index if not stack else (index - stack[-1][0] - 1)
                    area = heightpop * width
                    max_area = max(area, max_area)
                stack.append((index, height))

        n = len(heights)
        while stack:
            indexpop, heightpop = stack.pop()
            width = n if not stack else (n - stack[-1][0] - 1)
            area = heightpop * width
            max_area = max(max_area, area)
            
        return max_area