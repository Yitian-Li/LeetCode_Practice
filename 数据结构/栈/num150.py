class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return

        stack = []
        ops = {'+', '-', '*', '/'}

        for s in tokens:
            if s in ops:
                y = stack.pop()
                x = stack.pop()
                if s == '+':
                    stack.append(x + y)
                if s == '-':
                    stack.append(x - y)
                if s == '*':
                    stack.append(x * y)
                if s == '/':
                    stack.append(int(x / y))

            else:
                stack.append(int(s))

        return sum(stack)