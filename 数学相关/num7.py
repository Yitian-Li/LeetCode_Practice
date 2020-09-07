class Solution:
    def reverse(self, x: int) -> int:
        int_max = 2 ** 31 - 1
        int_min = 2 ** 31

        if x < 0:
            x = -x
            flag = -1
        else:
            flag = 1

        res = 0
        while x:
            pop = x % 10
            if flag == 1 and ((res == int_max // 10 and pop > 7) or res > int_max // 10):
                return 0
            if flag == -1 and ((res == int_min // 10 and pop > 8) or res > int_min // 10):
                return 0
            res = res * 10 + pop
            x = x // 10
        return flag * res


s = Solution()
print(s.reverse(1534236469))
