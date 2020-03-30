class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # heights = [2, 1, 2]
        heights = [0] + heights + [0]
        stack = [0]
        ans = 0

        for i in range(1, len(heights)):
            # print(stack, i)
            while heights[i] < heights[stack[-1]]:
                cur = stack.pop()
                ans = max(ans, heights[cur] * (i - stack[-1] - 1))
                
            stack.append(i)

        return ans