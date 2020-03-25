class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def search(nums, left, right, target):
            if left < right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return search(nums, mid+1, right, target)
                else:
                    return search(nums, left, mid-1, target)
            else:
                if target > nums[left]: return left+1
                else: return left

        if len(nums) == 0:
            return 0
            
        left, right = 0, len(nums)-1
        idx = search(nums, left, right, target)
        return idx