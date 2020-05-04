class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        stack = []
        sign = '+'

        for i in range(len(s)):
            ch = s[i]
            if '0' <= ch <= '9':
                num = num * 10 + int(ch)

            if ch in {'+', '-', '*', '/'} or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = ch

        return sum(stack)