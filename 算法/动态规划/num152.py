class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # imin, imax 记录以i位置为结尾的子数组，可以达到的最大负数、正数值
        ans = float('-inf')
        if len(nums) < 2:
            return nums[0]

        imin, imax = 1, 1
        for i in range(len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
                
            imin = min(nums[i], nums[i] * imin)
            imax = max(nums[i], nums[i] * imax)
            ans = max(imax, ans)
            # print(imin, imax, ans)

        return ans