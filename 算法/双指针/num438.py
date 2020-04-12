from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lens, lenp = len(s), len(p)
        need = {}
        for c in p:
            need[c] = need.get(c, 0) + 1

        ans = []
        left, right = 0, 0

        window = {}

        while right < lens:
            char = s[right]
            if char not in need:
                window.clear()
                right += 1
                left = right
            else:
                window[char] = window.get(char, 0) + 1
                if right - left + 1 == lenp:
                    if window == need:
                        ans.append(left)
                    window[s[left]] -= 1
                    left += 1
                right += 1
        return ans