class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = nums[0]
        for i in range(1, len(nums)):
            a ^= nums[i]
        return a