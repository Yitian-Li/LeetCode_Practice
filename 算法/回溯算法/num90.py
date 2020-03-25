class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, path):
            res.append(path)
            if not nums:
                return
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(nums[i+1:], path[:])
                path.pop()

        nums.sort()
        backtrack(nums, [])
        return res