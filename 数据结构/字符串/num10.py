class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p:
            return True

        if not s or not p:
            return False

        first_match = p[0] in (s[0], '*')

        if len(p) > 1 and p[1] == '*':
            return (first_match and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
        else:
            return first_match and self.isMatch(s[1:], p[1:])
