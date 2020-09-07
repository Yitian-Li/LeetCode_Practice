class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = (numRows - 1) * 2
        rows = [""] * numRows

        for i in range(len(s)):
            x = i % n
            y = min(x, n - x)
            rows[y] += s[i]

        return "".join(rows)