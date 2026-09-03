class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        myqueue = deque()
        INF = 2**31 - 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    myqueue.append(((i,j), 0))


        while myqueue:
            for i in range(len(myqueue)):
                (i,j), val = myqueue.popleft()
                for di, dj in [(0,1), (0,-1), (-1,0), (1,0)]:
                    vert = i + di
                    hor = j + dj
                    if vert >= 0 and hor>=0 and vert < len(grid) and hor < len(grid[0]):
                        if grid[vert][hor] == INF:
                            myqueue.append(((vert,hor), val+1))
                            grid[vert][hor] = val+1


        return