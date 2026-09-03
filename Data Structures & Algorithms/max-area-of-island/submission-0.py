class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        mymax = 0
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]

        def dfs(vert, hor):
            if vert < 0 or hor < 0 or vert >= len(grid) or hor >= len(grid[0]):
                return 0
            if visited[vert][hor] == 1 or grid[vert][hor] == 0:
                return 0

            visited[vert][hor] = 1
            return 1 + dfs(vert,hor-1) + dfs(vert,hor+1) + dfs(vert+1,hor) + dfs(vert-1,hor)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    cur = dfs(i,j)
                    mymax = max(cur, mymax)
    
                visited[i][j] = 1

        return mymax