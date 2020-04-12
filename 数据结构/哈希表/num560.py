class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        Sum = [0] * (len(nums))

        d = {0 : 1}
        s, cnt = 0, 0

        for i in range(len(nums)):
            s += nums[i]
            cnt += d.get(s - k, 0)
            d[s] = d.get(s, 0) + 1

        return cnt