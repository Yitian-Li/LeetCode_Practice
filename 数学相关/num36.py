class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:  
        # 规则1
        for i in range(9):
            flag = [0] * 9
            for j in range(9):
                item = board[i][j]
                if not item == '.' :
                    if flag[int(item)-1] == 0:
                        flag[int(item)-1] = 1
                    else:
                        return False

        # 规则2
        for j in range(9):
            flag = [0] * 9
            for i in range(9):
                item = board[i][j]
                if not item == '.' :
                    if flag[int(item)-1] == 0:
                        flag[int(item)-1] = 1
                    else:
                        return False

        # 规则3
        flatten = [j for i in board for j in i]
        start = [3*i + 27*j for j in range(3) for i in range(3)]
        add = [0, 1, 2, 9, 10, 11, 18, 19, 20]
        for i in start:
            flag = [0] * 9
            for j in add:
                item = flatten[i+j]
                if not item == '.' :
                    if flag[int(item)-1] == 0:
                        flag[int(item)-1] = 1
                    else:
                        return False
        return True