class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        ans = 0
        chars_cnt = collections.Counter(chars)
        for word in words:
            word_cnt = collections.Counter(word)
            if all(word_cnt[item] <= chars_cnt[item] for item in word_cnt):
                ans += len(word)
        return ans