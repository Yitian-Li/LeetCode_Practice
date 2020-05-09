class Solution:
    def totalNQueens(self, n: int) -> int:
        def can_put(i, j):
            return rows[j] == 0 and hills[i - j] == 0 and dales[i + j] == 0

        def place_queen(i, j):
            rows[j] = 1
            hills[i - j] = 1  # "hill" diagonals
            dales[i + j] = 1  # "dale" diagonals

        def remove_queen(i, j):
            rows[j] = 0
            hills[i - j] = 0  # "hill" diagonals
            dales[i + j] = 0  # "dale" diagonals

        def backtrack(i=0, count=0):
            for j in range(n):
                if can_put(i, j):
                    place_queen(i, j)
                    if i + 1 == n:
                        count += 1
                    else:
                        count = backtrack(i + 1, count)
                    remove_queen(i, j)
            return count

        rows = [0] * n
        hills = [0] * (2 * n - 1)  # "hill" diagonals
        dales = [0] * (2 * n - 1)  # "dale" diagonals
        return backtrack()


s = Solution()
print(s.totalNQueens(3))
