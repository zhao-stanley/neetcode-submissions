from collections import deque

class Solution:
    def get_neighbors(self, grid: List[List[str]], point: tuple[int, int]):
        row, col = point
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]
        neighbors = []

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbors.append((nr, nc))

        return neighbors

    def bfs(self, grid: List[List[str]], start: tuple[int, int], lands):
        row, col = start

        if grid[row][col] == "1":
            lands.add(start)

        q = deque([start])

        while q:
            current = q.popleft()
            for neighbor in self.get_neighbors(grid, current):
                nr, nc = neighbor
                if neighbor not in lands and grid[nr][nc] == "1":
                    lands.add(neighbor)
                    q.append(neighbor)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        lands = set()
        num_islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                cell = (row, col)
                if grid[row][col] == "1" and cell not in lands:
                    self.bfs(grid, cell, lands)
                    num_islands += 1

        return num_islands