class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt = {}
        for x in nums:
            if x in cnt:
                cnt[x] += 1
            else:
                cnt[x] = 1

        tosort = []
        for key in cnt:
            tosort.append([key, cnt[key]])
        tosort.sort(key=lambda x: x[1], reverse=True)

        ans = []
        for i in range(k):
            ans.append(tosort[i][0])
        
        return ans