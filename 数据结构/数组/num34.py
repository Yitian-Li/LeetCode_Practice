class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search(nums, left, right, target):
            while(left<=right):
                index = (left+right) // 2
                if nums[index] == target:
                    return index
                elif nums[index] > target:
                    return search(nums, left, index-1, target)
                elif nums[index] < target:
                    return search(nums, index+1, right, target)
            return -1

        def enlargeRange(nums, index):
            left = index
            right = index
            while left > -1 and nums[left]==nums[index]:
                left -= 1
            while right < len(nums) and nums[right]==nums[index]:
                right += 1
            return [left+1, right-1]


        size = len(nums)
        if size == 0:
            return [-1,-1]
        left = 0
        right = size-1

        index = search(nums, left, right, target)

        if index == -1:
            return [-1, -1]

        return enlargeRange(nums, index)
