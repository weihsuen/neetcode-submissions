class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for row in board:
            myList = []
            for i in range(9):
                if row[i]!= '.' and row[i] in myList:
                    return False
                elif row[i]!= '.':
                    myList.append(row[i])

        #check columns
        for i in range(9): #0
            myList = []
            for j in range(9): 
                if board[j][i]!= '.' and board[j][i] in myList:
                    return False
                elif board[j][i]!= '.':
                    myList.append(board[j][i])

        #check subboxes
        for i in range(0,9,3):
            for j in range(0,9,3):
                myList = []
                for a in range(3):
                    for b in range(3):
                        if board[i+a][j+b]!= '.' and board[i+a][j+b] in myList:
                            return False
                        elif board[i+a][j+b]!= '.':
                            myList.append(board[i+a][j+b])
        
        return True

