class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = ' ' + s
        p = ' ' + p

        dp = [[False] * len(p) for _ in range(len(s))]
        dp[0][0] = True

        for i in range(1, len(p)):
            if p[i] == '*':
                dp[0][i] = dp[0][i-1]

        for i in range(1, len(s)):
            for j in range(1, len(p)):
                if p[j] in {s[i], '?'}:
                    dp[i][j] = dp[i-1][j-1]
                if p[j] == '*':
                    dp[i][j] = dp[i-1][j-1] or dp[i][j-1] or dp[i-1][j]
        
        return dp[-1][-1]   