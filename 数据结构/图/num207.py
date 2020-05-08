class Solution:
    def canFinish(self, numCourses: int, prerequisites: [[int]]):
        if not prerequisites:
            return True

        visited = [0] * numCourses
        graph = [set() for _ in range(numCourses)]

        for first, second in prerequisites:
            graph[first].add(second)

        res = []

        def dfs(i):
            if visited[i] == 2: return False
            if visited[i] == 1: return True

            visited[i] = 2
            for nxt in graph[i]:
                if not dfs(nxt):
                    return False
            visited[i] = 1

            # 从i开始学，如果没有循环
            res.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res


s = Solution()
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(s.canFinish(numCourses, prerequisites))
