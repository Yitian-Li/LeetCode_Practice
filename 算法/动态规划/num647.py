class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # dp[i][j]表示s[i:j+1]是否是回文子串
        dp = [[False] * n for _ in range(n)]
        ans = 0

        for j in range(n):
            for i in range(j+1):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    ans += 1
                    
        return ans