class Solution:
    def uniquePaths(self, col: int, row: int) -> int:
        grid = [[1]*row]*col
        # print(grid)
        for i in range(1, col):
            for j in range(1, row):
                grid[i][j]=grid[i-1][j]+grid[i][j-1]
                
        return grid[col-1][row-1]