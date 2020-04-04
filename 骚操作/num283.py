class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count0 += 1
            else:
                nums[i-count0] = nums[i]
        
        idx = len(nums) - 1
        while count0:
            nums[idx] = 0
            count0 -= 1
            idx -= 1