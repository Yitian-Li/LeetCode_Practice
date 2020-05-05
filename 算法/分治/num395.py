from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        d = Counter(s)
        for c in d:
            if d[c] < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)