class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxarea = 0
        if not matrix or not matrix[0]:
            return maxarea

        m, n = len(matrix), len(matrix[0])
        heights = [0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            maxarea = max(maxarea, self.largestRectangleArea(heights))
        return maxarea

    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = [0]
        ans = 0
        for i in range(1, len(heights)):
            while heights[i] < heights[stack[-1]]:
                cur = stack.pop()
                ans = max(ans, heights[cur] * (i - stack[-1] - 1))
                
            stack.append(i)
        return ans