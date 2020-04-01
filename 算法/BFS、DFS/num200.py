class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        grid = self.padding(grid)
        m, n = len(grid), len(grid[0])
        ans = 0

        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == 1:
                    ans += 1
                    self.dfs(grid, i, j)

        return ans

    def padding(self, grid):
        m, n = len(grid), len(grid[0])
        new_grid = [[0]*(n+2) for i in range(m+2)]

        for i in range(m):
            for j in range(n):
                new_grid[i+1][j+1] = int(grid[i][j])

        return new_grid

    def dfs(self, grid, i, j):
        grid[i][j] = 0
        if grid[i-1][j]: self.dfs(grid, i-1, j)
        if grid[i+1][j]: self.dfs(grid, i+1 ,j)
        if grid[i][j+1]: self.dfs(grid, i, j+1)
        if grid[i][j-1]: self.dfs(grid, i, j-1)