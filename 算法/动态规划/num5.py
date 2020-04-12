class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans, n = "", len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for j in range(n):
            for i in range(j+1):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and len(s[i:j+1]) > len(ans):
                    ans = s[i:j+1]
        return ans