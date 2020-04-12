class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                # stack保存括号外的字符串，以及倍数
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                # 计算括号里的结果，并与括号外的字符串拼接起来
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                # 计算k
                multi = multi * 10 + int(c)            
            else:
                # res保存当前字符串
                res += c
        return res
