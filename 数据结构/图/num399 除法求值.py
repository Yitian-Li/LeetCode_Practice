class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        n = len(equations)
        Map = {}
        cnt = 0


        for i in range(n):
            x, y = equations[i][0], equations[i][1]
            if x not in Map:
                Map[x] = cnt
                cnt += 1
            if y not in Map:
                Map[y] = cnt
                cnt += 1

        size = len(Map)
        graph = [[0] * size for _ in range(size)]

        for i in range(n):
            x, y, k = equations[i][0], equations[i][1], values[i]
            graph[Map[x]][Map[y]] = k
            graph[Map[y]][Map[x]] = 1/k

        # 返回s到t的路径
        def dfs(s, t):
            visited.add(s)

            if s == t:
                return 1

            if graph[s][t]:
                return graph[s][t]

            for i in range(size):
                # s可以到达一个从未到达的结点i，然后从i出发，试试能不能到达t
                if graph[s][i] and i not in visited:
                    v = dfs(i, t)
                    if v != -1:
                        return graph[s][i] * v

            return -1

        # for r in graph:
        #     print(r)

        res = []
        for qs, qt in queries:
            if qs in Map and qt in Map:
                qs = Map[qs]
                qt = Map[qt]
                visited = set()
                res.append(dfs(qs, qt))
            else:
                res.append(-1)
        return res


# if __name__=='__main__':
#     sss = Solution()
#     equations = [["a", "b"], ["c", "d"], ["e", "f"], ["g", "h"]]
#     values = [4.5, 2.3, 8.9, 0.44]
#     queries = [["a", "c"], ["d", "f"], ["h", "e"], ["b", "e"], ["d", "h"], ["g", "f"], ["c", "g"]]
#     print(sss.calcEquation(equations, values, queries))