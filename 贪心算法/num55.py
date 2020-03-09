class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        MaxJump = 0
        for i in range(len(nums)):
            if i > MaxJump:
                return False
            MaxJump = max(MaxJump, nums[i]+i)
        return True