class Solution(object):
    def longestOnes_concise(self, A, K):
        left, right, count = 0, 0, 0  # 本来定义了max_len用来实时记录窗口大小，但后来发现非必要,因为窗口大小没有变小
        for right in range(len(A)):
            if A[right] == 0:
                count += 1
            if count > K:
                if A[left] == 0:
                    count -= 1
                left += 1
        return right - left + 1


s = Solution()
res = s.longestOnes_concise([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
print(res)
