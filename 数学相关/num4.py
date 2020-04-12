class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def findMid(nums):
            if len(nums) % 2:
                return nums[len(nums) // 2]
            else:
                return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
                
        arr = []

        while nums1 and nums2:
            if nums1[0] <= nums2[0]:
                arr.append(nums1.pop(0))
            else:
                arr.append(nums2.pop(0))
        
        while nums1:
            arr.append(nums1.pop(0))
        while nums2:
            arr.append(nums2.pop(0))

        return findMid(arr)