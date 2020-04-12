class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left, right, size, ans = 0, 0, len(s), 0
        d = {}

        while right < size:
            # 没有重复继续扩大
            if s[right] not in d:
                d[s[right]] = right
                right += 1
                ans = max(ans, right - left)

            # 重复了就去掉重复
            else:
                tmp = d[s[right]] + 1
                for i in range(left, d[s[right]] + 1):
                    d.pop(s[i])
                left = tmp
        return ans