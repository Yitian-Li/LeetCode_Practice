class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        size1 = len(word1) + 1
        size2 = len(word2) + 1
        dp = [[0]*size2 for i in range(size1)]

        for i in range(size1):
            dp[i][0] = i
        for j in range(size2):
            dp[0][j] = j
        
        for i in range(1, size1):
            for j in range(1, size2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    ) + 1
        return dp[-1][-1]