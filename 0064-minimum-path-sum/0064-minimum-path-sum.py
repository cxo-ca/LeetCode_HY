class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)       # 행
        n = len(grid[0])    # 열

        for i in range(1, m):   # 위->아래
            grid[i][0] += grid[i - 1][0]

        for j in range(1, n):   # 왼쪽->오른쪽
            grid[0][j] += grid[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[m - 1][n - 1]