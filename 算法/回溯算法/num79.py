class Solution:
    def exist(self, board, word):
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        maked = [[False] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if self.backtrack(board, word, (i, j), directions, maked, m, n):
                    return True
        return False
        # return self.backtrack(board, word, (0, 0), directions, maked, m, n)

    def backtrack(self, board, word, start, directions, maked, m, n):
        if len(word) == 1:
            return board[start[0]][start[1]] == word[0]
        # 如果当前位置正确
        if board[start[0]][start[1]] == word[0]:
            # 做选择
            maked[start[0]][start[1]] = True
            # 4个方向中选一个方向
            for direction in directions:
                new_start = (start[0] + direction[0], start[1] + direction[1])
                # 超过边界或者已经选择过
                if new_start[0] >= m or new_start[1] >= n or new_start[0] < 0 or new_start[1] < 0 or \
                        maked[new_start[0]][new_start[1]]:
                    continue
                elif self.backtrack(board, word[1:], new_start, directions, maked, m, n):
                    return True
            # 撤销选择
            maked[start[0]][start[1]] = False
        return False