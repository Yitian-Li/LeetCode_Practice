class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(1, len(s) + 1):
            if 1 <= int(s[i - 1]) <= 9:
                dp[i] += dp[i - 1]

            if i > 1:
                if 10 <= int(s[i - 2]) * 10 + int(s[i - 1]) <= 26:
                    dp[i] += dp[i - 2]

        return dp[-1]