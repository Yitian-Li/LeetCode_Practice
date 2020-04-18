class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        end = 0
        max_pos = 0
        for i in range(len(nums)-1):
            max_pos = max(max_pos, i + nums[i])
            
            if i == end:
                end = max_pos
                steps += 1

        return steps