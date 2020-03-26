from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""
        
        count_t = Counter(t)
        required = len(count_t)
        window_cnt = {}
        left, right = 0, 0
        got = 0
        ans = (False, 0, len(s)-1)
        while right < len(s):
            rs = s[right]
            window_cnt[rs] = window_cnt.get(rs, 0) + 1
            if rs in count_t and window_cnt[rs] == count_t[rs]:
                got += 1
            while left <= right and got == required:
                ls = s[left]
                window_cnt[ls] = window_cnt.get(ls, 0) - 1
                if ls in count_t and window_cnt[ls] < count_t[ls]:
                    got -= 1
                    if right - left <= ans[2] - ans[1]:
                        ans = (True, left, right)
                left += 1
            right += 1
        return "" if not ans[0] else s[ans[1]:ans[2]+1]