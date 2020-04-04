class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            stack = []
            for i in range(len(s)):
                if s[i] != '(' and s[i] != ')':
                    continue
                elif s[i] == '(':
                    stack.append('(')
                elif stack and s[i] == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')
            return not stack
        

        # BFS
        level = {s}  # 用set避免重复
        while True:
            valid = list(filter(isValid, level))  # 所有合法字符都筛选出来
            if valid: return valid # 如果当前valid是非空的，说明已经有合法的产生了
            # 下一层level
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] == '(' or item[i] == ')':  # 如果item[i]是个括号就删了
                        next_level.add(item[:i]+item[i+1:])
            level = next_level


