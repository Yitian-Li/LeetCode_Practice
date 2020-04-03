class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_area = 0
        if not matrix:
            return max_area

        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                dp[i][j] = int(matrix[i][j])
                max_area = max(dp[i][j], max_area)

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 1:
                    if i == 0 or j == 0:
                        continue
                    else:
                        dp[i][j]= min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                        max_area = max(max_area, dp[i][j]*dp[i][j])

        return max_area


# if __name__ == "__main__":
#     input = [["1", "0", "1", "0", "0", "1", "1", "1", "0"],
#              ["1", "1", "1", "0", "0", "0", "0", "0", "1"],
#              ["0", "0", "1", "1", "0", "0", "0", "1", "1"],
#              ["0", "1", "1", "0", "0", "1", "0", "0", "1"],
#              ["1", "1", "0", "1", "1", "0", "0", "1", "0"],
#              ["0", "1", "1", "1", "1", "1", "1", "0", "1"],
#              ["1", "0", "1", "1", "1", "0", "0", "1", "0"],
#              ["1", "1", "1", "0", "1", "0", "0", "0", "1"],
#              ["0", "1", "1", "1", "1", "0", "0", "1", "0"],
#              ["1", "0", "0", "1", "1", "1", "0", "0", "0"]]
#     s = Solution()
#     print(s.maximalSquare(input))
