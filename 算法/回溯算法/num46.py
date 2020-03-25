class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path):
            print(path, nums)
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                num = nums[i]
                path.append(num)
                backtrack(nums[:i]+nums[i+1:], path[:])
                path.pop()
        
        res = []
        backtrack(nums, [])
        return res