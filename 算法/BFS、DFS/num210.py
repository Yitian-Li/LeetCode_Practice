class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]

        adj_list = [set() for _ in range(numCourses)]
        visited = [0] * numCourses

        for cur, pre in prerequisites:
            adj_list[cur].add(pre) 

        def dfs(i):
            if visited[i] == 2:
                return True
            if visited[i] == 1:
                return False

            visited[i] = 2

            for p in adj_list[i]:
                if dfs(p): return True
            
            visited[i] = 1
            res.append(i)
            
            return False

        res = []
        for i in range(numCourses):
                if dfs(i):
                    return []
        
        return res

class Solution:
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