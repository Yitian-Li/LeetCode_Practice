class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        small = nums[0]
        mid = float('inf')

        for num in nums:
            if num <= small: small = num
            elif num <= mid: mid = num
            else: return True

        return False 