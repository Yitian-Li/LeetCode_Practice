def quick_s(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    else:
        return quick_s(n // 2) * quick_s(n - n // 2)

n = int(input())
print(quick_s(n))
