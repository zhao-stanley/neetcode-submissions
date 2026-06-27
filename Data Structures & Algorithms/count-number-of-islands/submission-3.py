from collections import deque

class Solution:
    def get_neighbors(self, grid: List[List[str]], point: tuple[int, int]):
        x = point[0]
        y = point[1]
        gw = len(grid[0])
        gh = len(grid)
        cells = [(0, 1), (-1, 0), (1, 0), (0, -1)]
        neighbors = []

        for cx, cy in cells:
            result_x = x + cx
            result_y = y + cy
            if 0 <= result_x < gh and 0 <= result_y < gw:
                neighbors.append((result_x, result_y))
        return neighbors


    def bfs(self, grid: List[List[str]], start: tuple[int, int], lands):
        starting_count = len(lands)
        sx, sy = start[0], start[1]

        if grid[sx][sy] == "1":
            lands.add(start)
        
        q = deque([start])

        while q:
            current = q.popleft()
            neighbors = self.get_neighbors(grid, current)
            for neighbor in neighbors:
                x = neighbor[0]
                y = neighbor[1]
                # only check land neighbors / add them to queue
                if neighbor not in lands and grid[x][y] == "1":
                    lands.add(neighbor)
                    q.append(neighbor)
            

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        lands = set()
        num_islands = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                cell = (r, c)
                # since we only check unvisited land, if we run bfs, we found a new island
                if grid[r][c] == "1" and cell not in lands:
                    self.bfs(grid, cell, lands)
                    num_islands += 1

        return num_islands