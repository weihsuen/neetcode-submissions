class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        #create visited array
        visited =  [ [0]*len(grid[0]) for _ in range(len(grid)) ]
        #create dfs search: find 1 in all directions and mark as visited
        def dfs(vert:int, hor:int):
            if vert < 0 or hor <0 or vert >= len(grid) or hor >= len(grid[0]):
                return
            if grid[vert][hor] == "0" or visited[vert][hor] == 1:
                return

            visited[vert][hor] = 1
            dfs(vert-1, hor)
            dfs(vert+1, hor)
            dfs(vert, hor-1)
            dfs(vert, hor+1)

        #traverse through 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == 0 and grid[i][j]=="1":
                    dfs(i,j)
                    count +=1
                elif visited[i][j]:
                    visited[i][j] = 1
        #if 1 and unvisited, do dfs, count +=1

        #if visited, continue
        return count
