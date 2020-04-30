class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        self.res = 0
        memo = {}

        def longestFromStart(matrix, i, j):
            # print("position:", (i, j), "=", matrix[i][j])
            if (i, j) in memo:
                return memo[(i, j)]
            else:
                tmp = 0
                if i + 1 < len(matrix) and matrix[i + 1][j] > matrix[i][j]:
                    tmp = max(tmp, longestFromStart(matrix, i + 1, j))
                if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                    tmp = max(tmp, longestFromStart(matrix, i - 1, j))
                if j + 1 < len(matrix[0]) and matrix[i][j + 1] > matrix[i][j]:
                    tmp = max(tmp, longestFromStart(matrix, i, j + 1))
                if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                    tmp = max(tmp, longestFromStart(matrix, i, j - 1))

                memo[(i, j)] = 1 + tmp
                self.res = max(self.res, memo[(i, j)])
                return memo[(i, j)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # print("--------------------")
                longestFromStart(matrix, i, j)

        return self.res