class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        if size < 3:
            return 0

        left = 0
        right = size -1
        left_max = height[left]
        right_max = height[right]
        ans = 0

        while left<right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        
        return ans