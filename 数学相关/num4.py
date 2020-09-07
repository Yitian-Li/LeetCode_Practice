class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        def findKth(k):
            index1, index2 = 0, 0
            while True:
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                new_index1 = min(m - 1, index1 + k // 2 - 1)
                new_index2 = min(n - 1, index2 + k // 2 - 1)
                pivot1, pivot2 = nums1[new_index1], nums2[new_index2]
                if pivot1 < pivot2:
                    k -= new_index1 - index1 + 1
                    index1 = new_index1 + 1
                else:
                    k -= new_index2 - index2 + 1
                    index2 = new_index2 + 1

        m, n = len(nums1), len(nums2)
        total_len = m + n
        if total_len % 2:
            return findKth(total_len // 2 + 1)
        else:
            return (findKth(total_len // 2) + findKth(total_len // 2 + 1)) / 2


s = Solution()
print(s.findMedianSortedArrays([1, 2], [3, 4]))
