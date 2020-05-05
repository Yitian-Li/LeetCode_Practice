class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        seen = [[False] * n for _ in matrix]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = []

        i, j, cnt, d = 0, 0, 0, 0
        while 1:
            if len(res) == m * n:
                break

            # 改变螺旋的方向
            next_i = i + directions[d][0]
            next_j = j + directions[d][1]
            if next_i in (-1, m) or next_j in (-1, n) or seen[next_i][next_j]:
                d = (d + 1) % 4

            res.append(matrix[i][j])
            seen[i][j] = True

            i += directions[d][0]
            j += directions[d][1]

        return res
