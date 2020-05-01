import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if len(buildings) == 0:
            return []

        points = []
        for l, r, h in buildings:
            points.append((l, -h, r))
            points.append((r, h, 0))

        points.sort()

        res = [[0, 0]]
        height = [[0, float('inf')]]

        for cur, h, right in points:
            while cur >= height[0][1]:
                heapq.heappop(height)

            if h < 0:
                heapq.heappush(height, [h, right])

            if res[-1][1] != -height[0][0]:
                res.append([cur, -height[0][0]])
        
        return res[1:]