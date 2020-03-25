class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.solved = False
        self.rowUsed = [[False] * 10 for i in range(9)]
        self.colUsed = [[False] * 10 for i in range(9)]
        self.boxUsed = [[False] * 10 for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.': 
                    num = int(board[i][j])
                    self.placeNum(board, num, i, j)
        
        self.backtrack(board, 0, 0)

    def placeNum(self, board, num, i, j):
        board[i][j] = str(num)
        self.rowUsed[i][num] = True
        self.colUsed[j][num] = True
        self.boxUsed[i//3 * 3 + j//3][num] = True
    
    def removeNum(self, board, num, i, j):
        board[i][j] = '.'
        self.rowUsed[i][num] = False
        self.colUsed[j][num] = False
        self.boxUsed[i//3*3 + j//3][num] = False

    def isValid(self, board, num, i, j):
        if self.rowUsed[i][num] == False \
        and self.colUsed[j][num] == False \
        and self.boxUsed[i//3*3 + j//3][num] == False:
            return True
        else:
            return False

    def placeNextNum(self, board, i, j):
        if i == 8 and j == 8:
            self.solved = True
        else:
            if j == 8:
                self.backtrack(board, i + 1, 0)
            else:
                self.backtrack(board, i, j + 1)

    def backtrack(self, board, i, j):
            """
            Backtracking
            """
            # if the cell is empty
            if board[i][j] == '.':
                # iterate over all numbers from 1 to 9
                for num in range(1, 10):
                    if self.isValid(board, num, i, j):
                        self.placeNum(board, num, i, j)
                        self.placeNextNum(board, i, j)
                        # if sudoku is solved, there is no need to backtrack
                        # since the single unique solution is promised
                        if not self.solved:
                            self.removeNum(board, num, i, j)
            else:
                self.placeNextNum(board, i, j)


