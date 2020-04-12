class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def backtrack(path, nums):
            if not nums:
                res.append(path)
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i-1] == nums[i]:
                    continue
                
                path.append(nums[i])
                backtrack(path[:], nums[:i] + nums[i+1:])
                path.pop()
                
        nums.sort()
        res = []
        if nums:
            backtrack([], nums)
        return res