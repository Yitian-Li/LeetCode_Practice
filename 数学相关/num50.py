class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        elif n < 0:
            return 1 / self.myPow(x, -n)

        elif n % 2:
            return x * self.myPow(x, n-1)

        else:
            m = self.myPow(x, n//2)
            return m * m