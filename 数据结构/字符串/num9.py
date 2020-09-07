class Solution:
    def isPalindrome(self, x: int) -> bool:
        c = str(x)
        if c == c[::-1]:
            return True
        else:
            return False