class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = [[False] * n for _ in range(m)]
        res = []
        i, j, idx = 0, 0, 0

        while len(res) < m * n:
            res.append(matrix[i][j])
            visited[i][j] = True
            next_i, next_j = i + directions[idx][0], j + directions[idx][1]
            if not (0 <= next_i < m and 0 <= next_j < n and not visited[next_i][next_j]):
                idx = (idx + 1) % 4
            i, j = i + directions[idx][0], j + directions[idx][1]
        return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = Solution()
res = s.spiralOrder(matrix)
print(res)
