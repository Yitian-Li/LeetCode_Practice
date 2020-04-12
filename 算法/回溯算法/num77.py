class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        nums = [i for i in range(1, n+1)]

        def backtrack(nums, path):
            if len(path) == k:
                res.append(path)
                return

            for i in range(len(nums)):
                if nums[i] in path:
                    continue

                path.add(nums[i])
                backtrack(nums[:i]+nums[i+1:], path.copy())
                path.remove(nums[i])

        res = []
        if nums: backtrack(nums, set())
        return res