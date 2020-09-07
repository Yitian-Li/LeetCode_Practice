class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left, right, size, ans = 0, 0, len(s), 0
        cur_s = dict()

        while size > right >= left:
            if s[right] in cur_s:
                cur_s.pop(s[left])
                left += 1
            else:
                cur_s[s[right]] = 1
                right += 1
            ans = max(ans, right - left)

        return ans

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))