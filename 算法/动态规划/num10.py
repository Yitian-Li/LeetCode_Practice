class Solution:

    def isMatch(self, s: str, p: str) -> bool:

        def matchs(i, j):
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        size_s = len(s)
        size_p = len(p)
        dp = [[False for _ in range(size_p + 1)] for _ in range(size_s + 1)]
        dp[0][0] = True

        for i in range(size_s + 1):
            for j in range(1, size_p + 1):

                if p[j - 1] == '*':
                    if matchs(i, j - 1):
                        dp[i][j] = (dp[i][j - 2] or dp[i - 1][j])
                    else:
                        dp[i][j] = dp[i][j - 2]

                else:
                    if matchs(i, j):
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = False
        return dp[-1][-1]


s = Solution()
print(s.isMatch("aa", "a"))
print(s.isMatch("aa", "a*"))
print(s.isMatch("ab", ".*"))
print(s.isMatch("aab", "c*a*b"))
print(s.isMatch("mississippi", "mis*is*p*."))
