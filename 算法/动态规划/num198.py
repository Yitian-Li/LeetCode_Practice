class Solution:
    def rob(self, nums: List[int]) -> int:
        curmax = 0
        premax = 0
        for i in range(len(nums)):
            temp = curmax
            curmax = max(nums[i] + premax, curmax)
            premax = temp

        return curmax