class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #travere top
        #traverse left
        #traverse right
        #traverse bottom
        visited = []

        
        def dfs(vert, hor):
            visited.append((vert, hor))
            if board[vert][hor] == "X":
                return
            else:
                board[vert][hor] = "S"
        
            for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
                ky, kx = dy+vert, dx+hor
                if 0 <= ky < len(board) and 0 <= kx < len(board[0]) and (ky, kx) not in visited:
                    dfs(ky, kx)


        for i in range(len(board)): #vert
            for j in range(len(board[0])-1): #hor
                if board[0][j] == "O": #top
                    dfs(0, j)
                if board[i][0] == "O": #left
                    dfs(i,0)
                if board[i][len(board[0])-1] == "O":
                    dfs(i, len(board[0])-1)
                if board[len(board)-1][j] == "O":
                    dfs(len(board)-1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                cur = board[i][j]
                if cur == "S":
                    board[i][j] = "O"
                if cur == "O":
                    board[i][j] = "X" 

          
        
                

