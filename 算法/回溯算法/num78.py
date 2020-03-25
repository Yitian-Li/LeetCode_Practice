class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, path):
            res.append(path)
            if not nums:
                return
            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(nums[i+1:], path[:])
                path.pop()

        backtrack(nums, [])
        return res