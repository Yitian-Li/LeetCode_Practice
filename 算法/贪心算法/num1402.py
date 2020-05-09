class Solution:
    def maxSatisfaction(self, satisfaction: [int]):
        if not satisfaction:
            return 0

        sum, res = 0, 0
        satisfaction.sort(reverse=True)
        for i in range(len(satisfaction)):
            sum += satisfaction[i]
            if sum > 0:
                res += sum
            else:
                break

        return res


s = Solution()
print(s.maxSatisfaction([-1, -8, 0, 5, -9]))
