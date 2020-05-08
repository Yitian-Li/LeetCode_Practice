class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = []

        i, j, cnt, d = 0, 0, 0, 0
        while 1:
            if len(res) == m * n:
                break

            # 改变螺旋的方向
            next_i = i + directions[d][0]
            next_j = j + directions[d][1]
            if next_i in (-1, m) or next_j in (-1, n) or matrix[next_i][next_j] == '#':
                d = (d + 1) % 4

            res.append(matrix[i][j])
            matrix[i][j] = '#'

            i += directions[d][0]
            j += directions[d][1]

        return res


s = Solution()
print(s.spiralOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
