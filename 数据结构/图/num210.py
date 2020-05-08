class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]

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

            # 从i开始学，如果没有循环，则依次添加nth....3rd，2nd，1st
            res.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res


class Solution2:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]

        adj_list = [set() for _ in range(numCourses)]
        in_degrees = [0] * numCourses

        for second, first in prerequisites:
            in_degrees[second] += 1
            adj_list[first].add(second)

        queue = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        res = []
        while queue:
            i = queue.pop(0)
            res.append(i)

            for p in adj_list[i]:
                in_degrees[p] -= 1
                if in_degrees[p] == 0:
                    queue.append(p)
        
        return res if len(res) == numCourses else []