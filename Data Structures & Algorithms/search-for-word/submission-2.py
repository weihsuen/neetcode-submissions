class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[0]*len(board[0]) for _ in range(len(board))]
        def backtrack(hor, ver, wordindex):
            if wordindex == len(word):
                return True

            if hor >= len(board) or hor < 0 or ver >= len(board[0]) or ver <0:
                return False

            if visited[hor][ver] or board[hor][ver] != word[wordindex]:
                return False

            visited[hor][ver] = 1
            found = (backtrack(hor, ver-1, wordindex+1) or
                    backtrack(hor+1, ver, wordindex+1) or 
                    backtrack(hor-1, ver, wordindex+1) or
                    backtrack(hor, ver+1, wordindex+1))

            visited[hor][ver] = 0
            return found

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True

        return False
        