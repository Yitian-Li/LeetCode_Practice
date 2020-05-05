class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return board

        m, n = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != 'O':
                return

            # K代表不符合题意的O，没有被包围的O
            board[i][j] = 'K'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # 从边缘部分开始遍历，即找到没有被包围的O
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                board[i][j] = 'O' if board[i][j] == 'K' else 'X'