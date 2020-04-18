class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1

        for i in range(len(nums)):
            if nums[i] < 1 or nums[i] >= len(nums)+1:
                nums[i] = 1
        
        for i in range(len(nums)):
            a = abs(nums[i])
            nums[a-1] = - abs(nums[a-1])

        for idx, x in enumerate(nums):
            if x > 0:
                return idx + 1

        return len(nums) + 1