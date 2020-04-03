class Solution:
    def canFinish(self, numCourses, prerequisites):

        def bfs(numCourses, pres, in_count):
            queue = []
            for i in range(numCourses):
                if in_count[i] == 0:
                    queue.append(i)
            while queue:
                # print(queue)
                cur = queue[0]
                queue.pop(0)
                numCourses -= 1
                for pre in pres[cur]:
                    in_count[pre] -= 1
                    if in_count[pre] == 0:
                        queue.append(pre)
            if numCourses == 0:
                return True
            else:
                return False

        def dfs(flags, pres, i):
            # 从第i个课程开始，检查是否有环
            if flags[i] == -1: return True
            if flags[i] == 1: return False
            flags[i] = 1
            for j in pres[i]:
                # flags[j] = 1
                if not dfs(flags, pres, j): return False
            flags[i] = -1
            return True


        pres = [[] for _ in range(numCourses)]
        in_count = [0] * numCourses

        for (i, j) in prerequisites:
            pres[i].append(j)
            in_count[j] += 1

        flags = [0] * numCourses

        bfs(numCourses, pres, in_count)
        for i in range(numCourses):
            if not dfs(flags, pres, i):
                # print("dfs no")
                return False
        return True



if __name__ == "__main__":
    numCourses = 4
    prerequisites = [[0, 1], [1, 3], [2, 3]]
    s = Solution()
    s.canFinish(numCourses, prerequisites)