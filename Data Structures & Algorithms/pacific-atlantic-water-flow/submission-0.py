class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = []
        pacific = []
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        rows, cols = len(heights), len(heights[0])

        def recur(vert, hor, visited):
            visited.append((vert, hor))
        

            for dy, dx in directions:
                ky = dy + vert
                kx = dx + hor
                if ky >= 0 and kx >=0 and ky < len(heights) and kx < len(heights[0]):
                    if heights[ky][kx] >= heights[vert][hor] and (ky, kx) not in visited:
                        recur(ky, kx, visited)

        
            
        # Pacific borders (top row and left col)
        for i in range(rows):
            recur(i, 0, pacific)
        for j in range(cols):
            recur(0, j, pacific)

        # Atlantic borders (bottom row and right col)
        for i in range(rows):
            recur(i, cols - 1, atlantic)
        for j in range(cols):
            recur(rows - 1, j, atlantic)
            
        return list(set(atlantic) & set(pacific))