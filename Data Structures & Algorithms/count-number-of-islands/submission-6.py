class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col):
            if row >= ROWS or row < 0 or col >= COLS or col < 0 or grid[row][col] == "0":
                return

            grid[row][col] = "0"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)


        i = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" :
                    i += 1
                    dfs(r, c)

        return i
