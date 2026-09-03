class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        myqueue = deque()
        mymin = 0 
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    myqueue.append(((i,j),0))
            
                    

        while myqueue:
            (vert, hor), val = myqueue.popleft()
            ans +=1
            for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
                ky = dy + vert
                kx = dx + hor
                if ky >= 0 and kx >=0 and ky < len(grid) and kx < len(grid[0]):
                    if grid[ky][kx] == 1:
                        flag = 1
                        grid[ky][kx] = 2
                        mymin = max(mymin, val+1)
                        myqueue.append(((ky, kx), val+1))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return mymin
        

        
