class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        seen = set()

        def neighbors(src):
            r, c = src
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
            result = []

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1" and (nr, nc) not in seen:
                    result.append((nr, nc))  

            return result

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in seen:
                    islands += 1

                    q = deque([(r, c)])
                    seen.add((r, c))

                    while q:
                        src = q.popleft()
                        for neighbor in neighbors(src):
                            seen.add(neighbor)
                            q.append(neighbor)

        
        return islands