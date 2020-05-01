class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        flag = 1 if numerator * denominator >= 0 else -1
        numerator = abs(numerator)
        denominator = abs(denominator)  # python对于负数的除法依然是向下取整，题中的要求是按照绝对值除法余数的，所以取绝对值

        head = numerator // denominator
        head = str(head) if flag > 0 else '-' + str(head)

        rest = numerator % denominator
        res = []
        idx = 0
        d = {}

        while (rest != 0 and rest not in d):
            d[rest] = idx
            rest *= 10
            res.append(str(rest // denominator))
            rest = rest % denominator
            idx += 1

        if not res:
            return str(head)
        if rest == 0:
            return head + '.' + ''.join(res)
        else:
            return head + '.' + ''.join(res[:d[rest]]) + '(' + ''.join(res[d[rest]:]) + ')'
