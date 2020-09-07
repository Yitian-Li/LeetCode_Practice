class Solution:
    def myAtoi(self, str: str) -> int:
        blank = ' '
        i = 0
        flag = 1
        b = True

        while i < len(str):
            if str[i] == blank and b:
                i += 1
            elif str[i] == '-' and b:
                flag = -1
                i += 1
                b = False
            elif str[i] == '+' and b:
                flag = 1
                i += 1
                b = False
            elif str[i] > '9' or str[i] < '0':
                return 0
            else:
                break

        left, right = -1, -1
        while i < len(str):
            if '0' <= str[i] <= '9':
                if left == -1:
                    left = i
                    right = i
                else:
                    right = i
                i += 1
            else:
                break

        if left == right == -1:
            return 0

        x = str[left:right + 1]
        x = int(x)
        if flag == -1 and x > 2 ** 31:
            return -2 ** 31
        if flag == 1 and x > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return flag * x


s = Solution()
res = s.myAtoi("3.14159")
print(res)
