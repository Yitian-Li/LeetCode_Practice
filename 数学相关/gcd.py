def gcd(x, y):
    """
    最大公约数
    辗转相除法
    """
    (x, y) = (y, x) if x < y else (x, y)
    remain = x % y
    while remain:
        x, y = y, remain
        remain = x % y
    return y


def lcd(x, y):
    """
    两个数的乘积等于这两个数的最大公约数与最小公倍数的积
    """
    return  x*y//gcd(x,y)



print(gcd(319, 377))
print(gcd(98, 63))
print(lcd(18, 20))
